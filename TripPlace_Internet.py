# -*- coding: cp949 -*-
from TripPlace_XML import *
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer

##global
conn = None
#arcode = None   #������ȣ

regKey = 'nHhF%2FXpBrln%2Fp4eurQr9Hn0sY0dZMB9Te%2ByR5uzHoZKpC%2BoE3ZwREHfHX3QJ%2FGsCXTm6%2FLgAZjZKqAEHLCy4pw%3D%3D'

#regKey = '9dc253be6f5224567ede1f03b84a4e24'

# ���̹� OpenAPI ���� ���� information
server = "api.visitkorea.or.kr"
#server = "apis.daum.net"

# smtp ����
host = "smtp.gmail.com"  # Gmail SMTP ���� �ּ�.
port = "587"


def userURIBuilderArea(server, key, areaCode, page):
    str = "http://" + server + "/openapi/service/rest/KorService/areaBasedList" + "?"

    if page == 1:
        str += "ServiceKey=" + key + "&" + "areaCode=" + areaCode + "&numOfRows=20&pageNo=1" �
                                                                "&MobileOS=ETC&MobileApp=AppTesting"
    return str

#http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?ServiceKey=����Ű&areaCode=35&MobileOS=ETC&MobileApp=AppTesting

def connectOpenAPIServer():
    global conn, server
    conn = HTTPConnection(server)


def getTripPlaceDataArea(areaCode, page):
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()
    # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)

    uri = userURIBuilderArea(server, regKey, areaCode, page)  # ���� �˻� URL
    conn.request("GET", uri)
    print(uri)

    req = conn.getresponse()

    if int(req.status) == 200:
        print("��� ������ ��� �޾ƿԽ��ϴ�")
        return extractTripPlaceData(req.read())
    else:
        print("���� ��� ������ �޾ƿ��� ���߽��ϴ�.")
        return None

def getTripPlaceDataCate(page):
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()
    # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
    uri = userURIBuilder(server, regKey, areaCode)  # ���� �˻� URL
    conn.request("GET", uri)
    print(uri)
    req = conn.getresponse()
    if int(req.status) == 200:
        print("��� ������ ��� �޾ƿԽ��ϴ�")
        return extractTripPlaceData(req.read())
    else:
        print("���� ��� ������ �޾ƿ��� ���߽��ϴ�.")
        return None


#������ ���� ��
def extractTripPlaceData(strXml):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    #print(strXml)
    # TripPlaceData(Book) ������Ʈ�� �����ɴϴ�.
    tripPlaceIndex = 1
    ####################��������?������������������ �������!!!!
    for item in tree.iter("item"):
        tripPlaceTitle = item.find("title")
        tripPlaceAddress = item.find("add1")
        tripPlaceTel = item.find("tel")
        print(tripPlaceIndex)
        print(tripPlaceTitle.text)
        if tripPlaceAddress != None:
            print(tripPlaceAddress.text)
        if tripPlaceTel != None:
            print(tripPlaceTel.text)
        print()
        tripPlaceIndex += 1

        #print("  " + tripPlaceTitle.text + "  ��ȣ : " + tripPlaceTel + "   �ּ� : " + tripPlaceAddress)

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
    #    return {"�ּ�": strAddress, "��ȣ": strNumber}
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
    # MIMEMultipart�� MIME�� �����մϴ�.
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # Message container�� �����մϴ�.
    msg = MIMEMultipart('alternative')

    # set message
    msg['Subject'] = title
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    msgPart = MIMEText(msgtext, 'plain')
    bookPart = MIMEText(html, 'html', _charset='UTF-8')

    # �޼����� ������ MIME ������ ÷���մϴ�.
    msg.attach(msgPart)
    msg.attach(bookPart)

    print("connect smtp server ... ")
    s = mysmtplib.MySMTP(host, port)
    # s.set_debuglevel(1)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, passwd)  # �α��� �մϴ�.
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
            html = MakeHtmlDoc(SearchBookTitle(value))  # keyword�� �ش��ϴ� å�� �˻��ؼ� HTML�� ��ȯ�մϴ�.
            ##��� �κ��� �ۼ�.
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))  # ����( body ) �κ��� ��� �մϴ�.
        else:
            self.send_error(400, ' bad requst : please check the your url')  # �� ���� ��û��� ������ �����Ѵ�.


def startWebService():
    try:
        server = HTTPServer(('localhost', 8080), MyHandler)
        print("started http server....")
        server.serve_forever()

    except KeyboardInterrupt:
        print("shutdown web server")
        server.socket.close()  # server �����մϴ�.


def checkConnection():
    global conn
    if conn == None:
        print("Error : ���� ����")
        return False
    return True
