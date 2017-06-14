# -*- coding: cp949 -*-
from Book_XML import *
from tkinter import *
from tkinter import font
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer

import urllib
import http.client

##global
conn = None

regKey = '9dc253be6f5224567ede1f03b84a4e24'

server = "apis.daum.net"

# smtp ����
host = "smtp.gmail.com"  # Gmail SMTP ���� �ּ�.
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
    conn = http.client.HTTPConnection(server)


def getBookData(g_Tk, area, page):
    global server, regKey, conn

    if conn == None:
        connectOpenAPIServer()

    uri = userURIBuilder(server, regKey, area, page)
    conn.request("GET", uri)
    print(uri)

    req = conn.getresponse()

    print(req.status)
    if int(req.status) == 200:
        print("å ������ ��� �޾ƿԽ��ϴ�")
        #return extractPreschoolData(req.read())

        return extractBookData(g_Tk, req.read().decode('utf-8'))
    else:
        print("���� å ������ �޾ƿ��� ���߽��ϴ�.")
        return None


def extractBookData(g_Tk, strXml):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)

    BookIndex = 1

    strOut = ""


    for item in tree.iter("item"):
        strAuthor = item.find("author")
        strCategory = item.find("category")
        strPrice = item.find("list_price")
        strTitle = item.find("title")

        if strTitle != None and strAuthor != None and strCategory != None and strPrice != None:
            print(BookIndex)
            print(strTitle.text)
            if len(strTitle.text) > 0:
                print("���� : " + strAuthor.text, "�з� : " + strCategory.text, "���� : " + strPrice.text)
                print(" ")

            strOut += """
            """
            strOut += "%d" %BookIndex + """
            """
            strOut += "  å ���� : " + strTitle.text + """
            """ + "  ���� : " + strAuthor.text + """
            """ + "  �з� : " + strCategory.text + """
            """ + "  ���� : " + strPrice.text + """
            """

            BookIndex += 1
        else:
            return None

    return strOut

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
