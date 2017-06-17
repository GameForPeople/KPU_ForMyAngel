from Product_XML import *
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer

import urllib
import http.client
import urllib.request

from tkinter import *

import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

##global
conn = None
#arcode = None   #지역번호

Key = '9dc253be6f5224567ede1f03b84a4e24'

#regKey = '9dc253be6f5224567ede1f03b84a4e24'

# 다음 OpenAPI 접속 정보 information
server = "apis.daum.net"
#server = "apis.daum.net"

#https://apis.daum.net/shopping/search?apikey={apikey}&q=신학기 가방&result=20&pageno=3&output=json&sort=min_price

# smtp 정보
host = "smtp.gmail.com"  # Gmail SMTP 서버 주소.
port = "587"


def userURIBuilder(server, key, question, page):
    str = "http://" + server + "/shopping/search" + "?"
    #for key in user.keys():
    #    str += "key" + key + "=" + user[key] + "&"
    hangul_utf8 = urllib.parse.quote(question)
    if page == 1:
        str += "apikey=" + key + "&" + "q=" + hangul_utf8 + "&result=20" + "&pageno=1" + "&output=xml" + "&sort=pop"
    elif page == 2:
        str += "apikey=" + key + "&" + "q=" + hangul_utf8 + "&result=20" + "&pageno=2" + "&output=xml" + "&sort=pop"
    elif page == 3:
        str += "apikey=" + key + "&" + "q=" + hangul_utf8 + "&result=20" + "&pageno=3" + "&output=xml" + "&sort=pop"
    return str

def connectOpenAPIServer():
    global conn, server
    #conn = HTTPConnection(server)
    conn = http.client.HTTPConnection("apis.daum.net")

def getProductData(g_Tk, question, page):
    global server, Key, conn
    if conn == None:
        connectOpenAPIServer()
    # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)

    uri = userURIBuilder(server, Key, question, page)  # 다음 검색 URL
    conn.request("GET", uri)
    print(uri)

    req = conn.getresponse()
    #print(req.status, req.reason)

    if int(req.status) == 200:
        print("물품 정보를 모두 받아왔습니다")
        #return extractProductData(req.read())
        return extractProductData(g_Tk, req.read().decode('utf-8'))
    else:
        print("역시 물품 정보는 받아오지 못했습니다.")
        return None


def DestoryItemLabel():
    itemLabel.destroy()

#끄집어 내는 곳
def extractProductData(g_Tk, strXml):
    from xml.etree import ElementTree
    global itemLabel

    tree = ElementTree.fromstring(strXml)
    #print(strXml)
    # ProductData(Book) 엘리먼트를 가져옵니다.
    ProductIndex = 1
    strOut = ""

    ####################성공한코듴ㅋㅋㅋㅋㅋㅋㅋㅋㅋ 왕좋고요!!!!
    for item in tree.iter("item"):
        ProductTitle = item.find("title")
        ProductPrice = item.find("price_min")
        ProductBrand = item.find("brand")
        ProductCategory = item.find("category_name")
        ProductImg = item.find("image_url")
    #<category_name>

        print(ProductIndex)

        strOut += """
        """
        strOut += """
        """

        if ProductBrand != None:
            print(ProductBrand.text)
            strOut += "제품 브랜드 : " + ProductBrand.text + """
            """

        print(ProductTitle.text)
        print(ProductCategory.text)

        strOut += "제품 이름 : " + ProductTitle.text + """
        """
        strOut += "제품 분류 : " + ProductCategory.text + """
        """

        if ProductPrice != None:
            print(ProductPrice.text)
            strOut += "제품 가격 : " + ProductPrice.text + """
            """

        if ProductImg != None:
            print(ProductImg.text)

           # urllib.request.urlretrieve(ProductImg.text, "productImg.jpg")

            #imgPath = "productImg.jpg"
            #photo = PhotoImage(file=imgPath)
            #label = Label(image=photo)
            #label.image = photo  # keep a reference!
            #label.place(x=20, y=300)
            urllib.request.urlretrieve(ProductImg.text, "productImg.jpg")

            #"https: // maps.googleapis.com / maps / api / staticmap?center = Brooklyn + Bridge, New + York, NY & zoom = 13 & size = 600x300 & maptype = roadmap& markers = color:blue % 7Clabel:S % 7C40.702147, -74.015794 & markers = color:green % 7Clabel:G % 7C40.711614, -74.012318& markers = color:red % 7Clabel:C % 7C40.718217, -73.998284& key = AIzaSyAJuhQwWPjYtXfS40mapKQIJsd2xV4cQHU"

            u = urllib.request.urlopen(ProductImg.text)
            raw_data = u.read()
            u.close()

            im = Image.open(BytesIO(raw_data))
            photo = ImageTk.PhotoImage(im)

            itemLabel = tk.Label(image=photo)
            itemLabel.image = photo
            itemLabel.pack()
            itemLabel.place(x=170, y = 540)


        print()
        ProductIndex += 1
        return strOut

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
