# -*- coding: cp949 -*-
from Book_XML import *
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer

import urllib
import http.client

##global
conn = None
#arcode = None   #지역번호

regKey = '9dc253be6f5224567ede1f03b84a4e24'
#regKey = 'nHhF%2FXpBrln%2Fp4eurQr9Hn0sY0dZMB9Te%2ByR5uzHoZKpC%2BoE3ZwREHfHX3QJ%2FGsCXTm6%2FLgAZjZKqAEHLCy4pw%3D%3D'

#server = "openapi.cpf.go.kr"
#server = "api.childcare.go.kr"
server = "apis.daum.net"

# smtp 정보
host = "smtp.gmail.com"  # Gmail SMTP 서버 주소.
port = "587"


def userURIBuilder(server, key, question, page):
    str = "https://" + server + "/search/book" + "?"

    hangul_utf8 = urllib.parse.quote(question)

    if page == 1:
        str += "apikey=" + key + "&" + "q=" + hangul_utf8 + "&output=xml&result=20" + "&pageno=1"
    elif page == 2:
        str += "apikey=" + key + "&" + "q=" + hangul_utf8 + "&output=xml&result=20" + "&pageno=2"
    elif page == 3:
        str += "apikey=" + key + "&" + "q=" + hangul_utf8 + "&output=xml&result=20" + "&pageno=3"

    return str

def connectOpenAPIServer():
    global conn, server
    #conn = HTTPConnection(server)
    conn = http.client.HTTPConnection(server)


def getBookData(area, page):
    global server, regKey, conn

    if conn == None:
        connectOpenAPIServer()

    uri = userURIBuilder(server, regKey, area, page)
    conn.request("GET", uri)
    print(uri)

    req = conn.getresponse()

    print(req.status)
    if int(req.status) == 200:
        print("책 정보를 모두 받아왔습니다")
        #return extractPreschoolData(req.read())
        extractBookData(req.read().decode('utf-8'))
        return None
    else:
        print("역시 책 정보는 받아오지 못했습니다.")
        return None


def extractBookData(strXml):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    #print(strXml)
    # PreschoolData(Book) 엘리먼트를 가져옵니다.
    #itemElements = tree.getiterator("item")  # return list type
    #print(itemElements)
    BookIndex = 1

    for item in tree.iter("item"):
        strAuthor = item.find("author")
        strCategory = item.find("category")
        strPrice = item.find("list_price")
        strTitle = item.find("title")

        if strTitle != None or strAuthor != None or strCategory != None or strPrice != None:
            print(BookIndex)
            print(strTitle.text)
            if len(strTitle.text) > 0:
                print("저자 : " + strAuthor.text, "분류 : " + strCategory.text, "가격 : " + strPrice.text)
                print(" ")
            BookIndex += 1
        else:
            return None


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
