from Hospital_XML import *
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib
import http.client


##global
conn = None
#arcode = None   #지역번호

Key = 'nHhF%2FXpBrln%2Fp4eurQr9Hn0sY0dZMB9Te%2ByR5uzHoZKpC%2BoE3ZwREHfHX3QJ%2FGsCXTm6%2FLgAZjZKqAEHLCy4pw%3D%3D'

#regKey = '9dc253be6f5224567ede1f03b84a4e24'

# 네이버 OpenAPI 접속 정보 information
server = "apis.data.go.kr"
#server = "apis.daum.net"

# smtp 정보
port = "587"
host = "smtp.gmail.com"  # Gmail SMTP 서버 주소.


def userURIBuilder(server, key, sidoCd, sgguCd, addr, page):
    str = "http://" + server + "/B551182/hospInfoService/getHospBasisList" + "?"
    #for key in user.keys():
    #    str += "key" + key + "=" + user[key] + "&"
    hangul_utf8 = urllib.parse.quote(addr)
#110000 110019
    if page == 1:
        str += "sidoCd="+ sidoCd +"&" + "sgguCd="+sgguCd+"&emdongNm=" + hangul_utf8 + "&pageNo=1"+ "&ServiceKey=" + key
    elif page == 2:
        str += "sidoCd="+ sidoCd +"&" + "sgguCd="+sgguCd+"&emdongNm=" + hangul_utf8 + "&pageNo=2"+ "&ServiceKey=" + key
    elif page == 3:
        str += "sidoCd="+ sidoCd +"&" + "sgguCd="+sgguCd+"&emdongNm=" + hangul_utf8 + "&pageNo=3"+ "&ServiceKey=" + key

    return str

def connectOpenAPIServer():
    global conn, server
    #conn = HTTPConnection(server)
    conn = http.client.HTTPConnection(server)

def getHospitalData(sidoCd, sgguCd, addr, page):
    global server, Key, conn
    if conn == None:
        connectOpenAPIServer()
    # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)

    uri = userURIBuilder(server, Key, sidoCd, sgguCd, addr, page)  # 다음 검색 URL
    conn.request("GET", uri)
    print(uri)

    req = conn.getresponse()
    print(req.status)

    if int(req.status) == 200:
        print("병원 정보를 모두 받아왔습니다")
        return extractHospitalData(req.read().decode('utf-8'))
    else:
        print("역시 병원 정보는 받아오지 못했습니다.")
        return None


#끄집어 내는 곳
def extractHospitalData(strXml):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    #print(strXml)
    # HospitalData(Book) 엘리먼트를 가져옵니다.
    HospitalIndex = 1
    ####################성공한코듴ㅋㅋㅋㅋㅋㅋㅋㅋㅋ 왕좋고요!!!!
    for item in tree.iter("item"):
        HospitalTitle = item.find("yadmNm")
        HospitalAddress = item.find("addr")
        HospitalTel = item.find("telno")
        print(HospitalIndex)
        print(HospitalTitle.text)
        if HospitalAddress != None:
            print(HospitalAddress.text)
        if HospitalTel != None:
            print(HospitalTel.text)
        print()
        HospitalIndex += 1

        #print("  " + tripPlaceTitle.text + "  번호 : " + tripPlaceTel + "   주소 : " + tripPlaceAddress)

    #####################
    #itemElements = tree.getiterator("item")  # return list type
    #print(itemElements)
    #for item in itemElements:
    #    #isbn = item.find("isbn")
    #    strTitle = item.find("title")
    #    strAddress = item.find("add1")
    #    strNumber = item.find("tel")
    #    print(item.get("title"))
    #    print(strTitle)
    #    #if len(strTitle.text) > 0:
    #    return {"주소": strAddress, "번호": strNumber}
    ########################


def sendMain():
    global host, port
    html = ""
    title = str(input('Title :'))
    senderAddr = str(input('sender email address :'))
    recipientAddr = str(input('recipient email address :'))
    msgtext = str(input('write message :'))
    passwd = str(input(' input your password of gmail account :'))
    msgtext = str(input('Do you want to include book data (y/n):'))
    if msgtext == 'y':
        keyword = str(input('input keyword to search:'))
        html = MakeHtmlDoc(SearchBookTitle(keyword))

    import mysmtplib
    # MIMEMultipart의 MIME을 생성합니다.
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # Message container를 생성합니다.
    msg = MIMEMultipart('alternative')

    # set message
    msg['Subject'] = title
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    msgPart = MIMEText(msgtext, 'plain')
    bookPart = MIMEText(html, 'html', _charset='UTF-8')

    # 메세지에 생성한 MIME 문서를 첨부합니다.
    msg.attach(msgPart)
    msg.attach(bookPart)

    print("connect smtp server ... ")
    s = mysmtplib.MySMTP(host, port)
    # s.set_debuglevel(1)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, passwd)  # 로긴을 합니다.
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()

    print("Mail sending complete!!!")


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        from urllib.parse import urlparse
        import sys

        parts = urlparse(self.path)
        keyword, value = parts.query.split('=', 1)

        if keyword == "title":
            html = MakeHtmlDoc(SearchBookTitle(value))  # keyword에 해당하는 책을 검색해서 HTML로 전환합니다.
            ##헤더 부분을 작성.
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))  # 본분( body ) 부분을 출력 합니다.
        else:
            self.send_error(400, ' bad requst : please check the your url')  # 잘 못된 요청라는 에러를 응답한다.


def startWebService():
    try:
        server = HTTPServer(('localhost', 8080), MyHandler)
        print("started http server....")
        server.serve_forever()

    except KeyboardInterrupt:
        print("shutdown web server")
        server.socket.close()  # server 종료합니다.


def checkConnection():
    global conn
    if conn == None:
        print("Error : 연결 실패")
        return False
    return True
