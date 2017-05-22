# -*- coding: 원성연 -*-
loopFlag = 1

from Preschool_Internet import *


#### Menu  implementation
def printMenu():
    print("₩n안녕하세요! For My Angel")
    print("========Menu==========")
    print("Show 유치원 : A ")
    print("Show 놀곳 : B ")
    print("Show 의료기관 : C ")
    print("Show 가격정보 : D ")
    print("프로그램 종료 : Q ")

"""
    print("Load xml:  l")
    print("Print dom to xml: p")
    print("Quit program:   q")
    print("print Book list: b")
    print("Add new book: a")
    print("sEarch Book Title: e")
    print("Make html: m")
    print("----------------------------------------")
    print("Get book data from isbn: g")
    print("send maIl : i")
    print("sTart Web Service: t")
    print("========Menu==========")
    """

def launcherFunction(menu):

    if menu == 'a':
        arccode = str(input ('arccode를 입력해주세요 : '))
        #arccode = '11380'
        getPreschoolDataFromArcode(arccode)
        #ret = getPreschoolDataFromArcode(arccode)
        #AddBook(ret)
        pass
    elif menu == 'b':
        pass
    elif menu == 'c':
        pass
    elif menu == 'd':
        pass
    elif menu == 'q':
        QuitProgram()
    else:
        print("정상적인 값을 넣어 주세요")

    """
    if menu == 'l':
        LoadXMLFromFile()
    elif menu == 'q':
        QuitBookMgr()
    elif menu == 'p':
        PrintDOMtoXML()
    elif menu == 'b':
        PrintBookList(["title", ])
    elif menu == 'a':
        ISBN = str(input('insert ISBN :'))
        title = str(input('insert Title :'))
        AddBook({'ISBN': ISBN, 'title': title})
    elif menu == 'e':
        keyword = str(input('input keyword to search :'))
        printBookList(SearchBookTitle(keyword))
    elif menu == 'g':
        isbn = str(input('input isbn to get :'))
        # isbn = '0596513984'
        ret = getBookDataFromISBN(isbn)
        AddBook(ret)
    elif menu == 'm':
        keyword = str(input('input keyword code to the html  :'))
        html = MakeHtmlDoc(SearchBookTitle(keyword))
        print("-----------------------")
        print(html)
        print("-----------------------")
    elif menu == 'i':
        sendMain()
    elif menu == "t":
        startWebService()
    else:
        print("error : unknow menu key")

    """
def QuitProgram():
    global loopFlag
    loopFlag = 0
    #BooksFree()


##### run #####
while (loopFlag > 0):
    printMenu()
    menuKey = str(input('원하는 기능을 입력해주세요 ------>  '))
    launcherFunction(menuKey)
else:
    print("응 끝!")
