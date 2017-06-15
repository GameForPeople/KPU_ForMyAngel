# -*- coding : cp949 -*-
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import html

import urllib
from tkinter import *
from tkinter import font

def SendEmail(g_Tk, msg):
    fromaddr = 'koreagamemaker@gmail.com'
    toaddr = 'koreagamemaker@gmail.com'
    #hangul_utf8 = urllib.parse.quote(msg)
    #sendIn = hangul_utf8
    sendIn = msg

    username = 'koreagamemaker'
    password = 'godnjs12com'

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)

    server.sendmail(fromaddr, toaddr, sendIn)
    server.quit()


def SendEmail2(g_Tk, msg):

    host = 'smtp.gmail.com'  # Gmail smtp server address
    port = '587'  # smtp port
    #htmlfile = 'logo.html'
    imagefile = 'productImg.jpg'
    msgText = msg

    sender = 'koreagamemaker@gmail.com'  # sender email address
    recipient = 'koreagamemaker@gmail.com'  # recipient email address

    # Create MIMEBase
    msg = MIMEBase('multipart', 'mixed')
    msg['Subject'] = 'ProductInternet_ForMyAngel'
    msg['From'] = sender
    msg['To'] = recipient

    # Create MIMEHtml
    #htmlF = open(htmlfile, 'rb')
    #htmlPart = MIMEText(htmlF.read(), 'html', _charset='utf-8')
    #htmlF.close()

    # Create MIMEImage
    imageF = open(imagefile, 'rb')
    imagePart = MIMEImage(imageF.read())
    imageF.close()

    msgPart = MIMEText(msgText, 'plain')

    # attach html,image
    msg.attach(imagePart)
    msg.attach(msgPart)
    #msg.attach(htmlPart)

    # mail send
    s = smtplib.SMTP(host, port)
    s.set_debuglevel(1)  # debuging
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(sender, 'godnjs12com')
    s.sendmail(sender, [recipient], msg.as_string())
    s.close()