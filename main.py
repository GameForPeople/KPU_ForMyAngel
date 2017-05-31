# -*- coding: 원성연 -*-
loopFlag = 1

from Preschool_Internet import *
from TripPlace_Internet import *
from Hospital_Internet import *
from Product_Internet import *


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
        isBook = True
        bookPage = 1
        bookQuestion = str(input('책과 관련된 정보를 입력해주세요 : '))

        while(isBook):
            getPreschoolDataFromArcode(bookQuestion, bookPage)

            bookBuffer = str(input ('다음페이지를 보시려면 Y, 다른 기능을 원하시면 N을 입력해주세요'))
            if bookPage == 3:
                print("")
                print("모든 결과를 열람하셨습니다. ")
                bookPage = 1
                isBook = False
            elif bookBuffer == 'Y':
                bookPage += 1
            elif bookBuffer == 'N':
                bookPage = 1
                isBook = False

        pass
    elif menu == 'b':
        isTrip = True
        tripPage = 1
        whatFunctionTrip = str(input('지역에 따른 검색은 A, 가족 추천 코스를 원하시면 B를 입력해주세요'))
        if whatFunctionTrip == 'a':
            areaCode = str(input('원하시는 지역을 입력해주세요 : '))

        while(isTrip):
            if whatFunctionTrip == 'a':
               getTripPlaceDataArea(areaCode, tripPage)
            elif whatFunctionTrip == 'b':
               getTripPlaceDataCate(tripPage)

            tripBuffer = str(input ('다음페이지를 보시려면 Y, 다른 기능을 원하시면 N을 입력해주세요'))
            if tripPage == 3:
                print("")
                print("모든 결과를 열람하셨습니다. ")
                tripPage = 1
                isTrip = False
            elif tripBuffer == 'Y':
                tripPage += 1
            elif tripBuffer == 'N':
                tripPage = 1
                isTrip = False

        pass
    elif menu == 'c':
        big = str(input ('시도코드를 입력해주세요 :  110000~ '))
        little = str(input ('시군구코드를 입력해주세요 : 110019 ~ '))
        #110000 110019
        getHospitalData(big, little)
        pass
    elif menu == 'd':
        questionInput = str(input ('상품 종류를 입력해주세요 :  '))
        getProductData(questionInput)
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
