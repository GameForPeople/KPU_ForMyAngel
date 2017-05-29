# -*- coding: cp949 -*-
from Preschool_XML import *
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer

##global
conn = None
#arcode = None   #������ȣ

regKey = '0c5747ff0e144b9ca77645c4ed19ef1b'

#regKey = '9dc253be6f5224567ede1f03b84a4e24'

# ���̹� OpenAPI ���� ���� information
server = "api.childcare.go.kr"
#server = "apis.daum.net"

# smtp ����
host = "smtp.gmail.com"  # Gmail SMTP ���� �ּ�.
port = "587"


def userURIBuilder(server, key, arcode):
    str = "http://" + server + "/mediate/rest/cpmsapi021/cpmsapi021/request" + "?"
    str += "key=" + key + "&" + "arcode=" + arcode
    return str

#http://api.childcare.go.kr/mediate/rest/cpmsapi021/cpmsapi021/request?key=50b8109640e3b5947a3788a03cfd151c&arcode=11380

def connectOpenAPIServer():
    global conn, server
    conn = HTTPConnection(server)


def getPreschoolDataFromArcode(arcode=11380):
    global server, regKey, conn

    print(" 1. �̺κ��� ������!!")
    if conn == None:
        connectOpenAPIServer()

    uri = userURIBuilder(server, regKey, arcode)
    print(uri)

    # ��Ȱ�ڵ� ������ ���� �Լ��κ��� �߰��մϴ�.
    #def userURIBuilder(server, key, arcode):
    #str = "http://" + server + "/mediate/rest/cpmsapi021/cpmsapi021/request" + "?"
    #str += "key=" + key + "&" + "arcode=" + arcode
    #return str


    print(" 2. �̺κ��� ������!!")
    conn.request("GET", uri)

    print(" 3. �̺κ��� ������!!")
    req = conn.getresponse()

    print(req.status)
    if int(req.status) == 200:
        print("��ġ�� ������ ��� �޾ƿԽ��ϴ�")
        return extractPreschoolData(req.read())
    else:
        print("���� ��ġ�� ������ �޾ƿ��� ���߽��ϴ�.")
        return None


def extractPreschoolData(strXml):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    print(strXml)
    # PreschoolData(Book) ������Ʈ�� �����ɴϴ�.
    itemElements = tree.getiterator("item")  # return list type
    print(itemElements)
    for item in itemElements:
        #isbn = item.find("isbn")
        strTitle = item.find("crname")
        strAddress = item.find("craddr")
        strNumber = item.find("crtel")

        print(strTitle)
        if len(strTitle.text) > 0:
            return {"�ּ�": strAddress.text, "��ȣ": strNumber.text}


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
