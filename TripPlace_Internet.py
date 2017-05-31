# -*- coding: cp949 -*-
from TripPlace_XML import *
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer

##global
conn = None
#arcode = None   #지역번호

regKey = 'nHhF%2FXpBrln%2Fp4eurQr9Hn0sY0dZMB9Te%2ByR5uzHoZKpC%2BoE3ZwREHfHX3QJ%2FGsCXTm6%2FLgAZjZKqAEHLCy4pw%3D%3D'

#regKey = '9dc253be6f5224567ede1f03b84a4e24'

# 네이버 OpenAPI 접속 정보 information
server = "api.visitkorea.or.kr"
#server = "apis.daum.net"

# smtp 정보
host = "smtp.gmail.com"  # Gmail SMTP 서버 주소.
port = "587"


def userURIBuilderArea(server, key, areaCode, page):
    str = "http://" + server + "/openapi/service/rest/KorService/areaBasedList" + "?"

    if page == 1:
        str += "ServiceKey=" + key + "&" + "areaCode=" + areaCode + "&numOfRows=20&pageNo=1&MobileOS=ETC&MobileApp=AppTesting"
    elif page == 2:
        str += "ServiceKey=" + key + "&" + "areaCode=" + areaCode + "&numOfRows=20&pageNo=2&MobileOS=ETC&MobileApp=AppTesting"
    elif page == 3:
        str += "ServiceKey=" + key + "&" + "areaCode=" + areaCode + "&numOfRows=20&pageNo=3&MobileOS=ETC&MobileApp=AppTesting"
    return str

def userURIBuilderCate(server, key, page):
    str = "http://" + server + "/openapi/service/rest/KorService/areaBasedList" + "?"

    if page == 1:
        str += "ServiceKey=" + key + "&" + "cat1=C01&cat2=C0112" + "&numOfRows=20&pageNo=1&MobileOS=ETC&MobileApp=AppTesting"
    elif page == 2:
        str += "ServiceKey=" + key + "&" + "cat1=C01&cat2=C0112" + "&numOfRows=20&pageNo=2&MobileOS=ETC&MobileApp=AppTesting"
    elif page == 3:
        str += "ServiceKey=" + key + "&" + "cat1=C01&cat2=C0112" + "&numOfRows=20&pageNo=3&MobileOS=ETC&MobileApp=AppTesting"
    return str

def connectOpenAPIServer():
    global conn, server
    conn = HTTPConnection(server)


def getTripPlaceDataArea(areaCode, page):
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()
    # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)

    uri = userURIBuilderArea(server, regKey, areaCode, page)  # 다음 검색 URL
    conn.request("GET", uri)
    print(uri)

    req = conn.getresponse()

    if int(req.status) == 200:
        print("놀곳 정보를 모두 받아왔습니다")
        return extractTripPlaceData(req.read())
    else:
        print("역시 놀곳 정보는 받아오지 못했습니다.")
        return None

def getTripPlaceDataCate(page):
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()
    # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
    uri = userURIBuilderCate(server, regKey, page)  # 다음 검색 URL
    conn.request("GET", uri)
    print(uri)
    req = conn.getresponse()
    if int(req.status) == 200:
        print("놀곳 정보를 모두 받아왔습니다")
        return extractTripPlaceData(req.read())
    else:
        print("역시 놀곳 정보는 받아오지 못했습니다.")
        return None


#끄집어 내는 곳
def extractTripPlaceData(strXml):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    #print(strXml)
    # TripPlaceData(Book) 엘리먼트를 가져옵니다.
    tripPlaceIndex = 1
    ####################성공한코?ㅋㅋㅋㅋㅋㅋㅋㅋㅋ 왕좋고요!!!!
    for item in tree.iter("item"):
        tripPlaceTitle = item.find("title")
        tripPlaceAddress = item.find("addr1")
        tripPlaceTel = item.find("tel")
        print(tripPlaceIndex)
        print(tripPlaceTitle.text)
        if tripPlaceAddress != None:
            print(tripPlaceAddress.text)
        if tripPlaceTel != None:
            print(tripPlaceTel.text)
        print()
        tripPlaceIndex += 1

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
