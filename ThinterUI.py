from tkinter import *
from tkinter import font

from Book_Internet import *
from Weather_internet import *
from TripPlace_Internet import *
from Hospital_Internet import *
from Product_Internet import *
from Mail_Function import *

import datetime

import playsound
import winsound

import tkinter.messagebox
g_Tk = Tk()
#g_Tk.geometry("400x600+750+200")
g_Tk.geometry("480x800+600+5")
g_Tk.title("""For My Angel  //게임공학과13학번원성연""")
DataList = []

BigButtonFont = font.Font(g_Tk, size=60, weight='bold', family='Consolas') #정식 버튼 글씨체
ButtonFont = font.Font(g_Tk, size=30, weight='bold', family='Consolas') #정식 버튼 글씨체
LittleLittleButtonFont = font.Font(g_Tk, size=11, weight='bold', family='Consolas') #정식 버튼 글씨체
LittleButtonFont = font.Font(g_Tk, size=16, weight='bold', family='Consolas') #정식 버튼 글씨체

photo_0 = PhotoImage(file="loadImg_0.png")  # 디폴트 이미지 파일
photo_1 = PhotoImage(file="loadImg_1.png")  # 디폴트 이미지 파일
photo_2 = PhotoImage(file="loadImg_2.png")  # 디폴트 이미지 파일
photo_3 = PhotoImage(file="loadImg_3.png")  # 디폴트 이미지 파일
photo_4 = PhotoImage(file="loadImg_4.png")  # 디폴트 이미지 파일
photo_5 = PhotoImage(file="loadImg_5.png")  # 디폴트 이미지 파일
photo_6 = PhotoImage(file="loadImg_6.png")  # 디폴트 이미지 파일
photo_7 = PhotoImage(file="loadImg_7.png")  # 디폴트 이미지 파일
photo_8 = PhotoImage(file="loadImg_8.png")  # 디폴트 이미지 파일
photo_9 = PhotoImage(file="loadImg_9.png")  # 디폴트 이미지 파일

iLoad = 0
isAni = False

INSERT_BUFFER = 0

ENTRY_BUFFER = Entry(g_Tk)

YES_BUTTON_BUFFER = Button(g_Tk)
NO_BUTTON_BUFFER = Button(g_Tk)
INSERT_BUTTON_BUFFER = Button(g_Tk)
MAIL_BUTTON_BUFFER = Button(g_Tk)

SCROLL_BAR = Scrollbar(g_Tk)
RENDER_TEXT = Text(g_Tk)
LABEL_BUFFER = Label(g_Tk)
MAIN_LABEL_BUFFER = Label(g_Tk)

imageLabel = Label(g_Tk, image=photo_0)
imageLabel.pack()

lab = Label(g_Tk)       #clock
lab.pack()

Page = 0

isItemImg = False
isMail = False
strOut = ""


def StartMail():
    global strOut
    SendEmail2(g_Tk, strOut)

def DeleteInfo():
    global YES_BUTTON_BUFFER, NO_BUTTON_BUFFER, SCROLL_BAR, RENDER_TEXT, INSERT_BUTTON_BUFFER, isMail, \
        MAIL_BUTTON_BUFFER, isItemImg, Page, MAIN_LABEL_BUFFER

    Page = 0

    YES_BUTTON_BUFFER.destroy()
    NO_BUTTON_BUFFER.destroy()

    SCROLL_BAR.destroy()
    RENDER_TEXT.destroy()

    ENTRY_BUFFER.destroy()
    LABEL_BUFFER.destroy()
    INSERT_BUTTON_BUFFER.destroy()

    MAIN_LABEL_BUFFER.destroy()

    if isMail == True:
        MAIL_BUTTON_BUFFER.destroy()
        isMail = False

    if isItemImg == True:
        DestoryItemLabel()
        isItemImg = False

    InitMenu()

def InsertBookInfo():
    global INSERT_BUFFER,Page, YES_BUTTON_BUFFER, NO_BUTTON_BUFFER, SCROLL_BAR, RENDER_TEXT, strOut, MAIN_LABEL_BUFFER

    YES_BUTTON_BUFFER.destroy()
    NO_BUTTON_BUFFER.destroy()

    MAIN_LABEL_BUFFER.destroy()
    SCROLL_BAR.destroy()
    RENDER_TEXT.destroy()

    Page += 1


    if Page == 4:
        print("")
        print("모든 결과를 열람하셨습니다. ")
        Page = 0
        DeleteInfo()
        return

    else:
        bookQuestion = ENTRY_BUFFER.get()
        print(bookQuestion)

        strOut = getBookData(g_Tk, bookQuestion, Page)

        SCROLL_BAR = Scrollbar(g_Tk)
        SCROLL_BAR.pack()
        SCROLL_BAR.place(x=470, y=200)
        TempFont = font.Font(g_Tk, size=10, family='Consolas')
        RENDER_TEXT = Text(g_Tk, width=60, height=41, borderwidth=12, relief='ridge',
                          yscrollcommand=SCROLL_BAR.set)
        RENDER_TEXT.pack()
        RENDER_TEXT.place(x=16, y=165)
        SCROLL_BAR.config(command=RENDER_TEXT.yview)
        SCROLL_BAR.pack(side=RIGHT, fill=BOTH)
        RENDER_TEXT.configure(state='normal')
        RENDER_TEXT.insert(INSERT, strOut)
        RENDER_TEXT["fg"] = "gray"

        #F = lambda bookBuffer, value : bookBuffer + value

        YES_BUTTON_BUFFER = Button(g_Tk,  font=LittleButtonFont, text="Next Page!", command=InsertBookInfo)

        if Page == 3:
            YES_BUTTON_BUFFER.configure(state="disabled")

        YES_BUTTON_BUFFER.pack()
        YES_BUTTON_BUFFER.place(x=320, y=730)
        YES_BUTTON_BUFFER["bg"] = "white"
        YES_BUTTON_BUFFER["fg"] = "pink"

        NO_BUTTON_BUFFER = Button(g_Tk,  font=LittleButtonFont, text="   Quit   ", command=DeleteInfo)
        NO_BUTTON_BUFFER.pack()
        NO_BUTTON_BUFFER.place(x=20, y=730)
        NO_BUTTON_BUFFER["bg"] = "white"
        NO_BUTTON_BUFFER["fg"] = "pink"

        MAIN_LABEL_BUFFER = Label(g_Tk, font=BigButtonFont , text="Book")
        MAIN_LABEL_BUFFER.pack()
        MAIN_LABEL_BUFFER.place(x=30, y=45)
        MAIN_LABEL_BUFFER["fg"] = "white"
        MAIN_LABEL_BUFFER["bg"] = "pink"

def FunctionBook():
    global INSERT_BUFFER, ENTRY_BUFFER, LABEL_BUFFER, INSERT_BUTTON_BUFFER

    winsound.PlaySound('effect_1.wav', winsound.SND_FILENAME)

    DestoryMenu()

    LABEL_BUFFER = Label(g_Tk, font=ButtonFont , text="About Book!")
    LABEL_BUFFER.place(x=120, y=240)
    LABEL_BUFFER["bg"] = "gray"
    LABEL_BUFFER["fg"] = "White"

    ENTRY_BUFFER = Entry(g_Tk , font=LittleButtonFont )
    ENTRY_BUFFER.pack()
    ENTRY_BUFFER.place(x=120, y=320)
    ENTRY_BUFFER["fg"] = "gray"

    INSERT_BUTTON_BUFFER = Button(g_Tk, font=LittleLittleButtonFont, text="검색", command = InsertBookInfo)
    INSERT_BUTTON_BUFFER.pack()
    INSERT_BUTTON_BUFFER.place(x=380, y=318)
    INSERT_BUTTON_BUFFER["bg"] = "white"
    INSERT_BUTTON_BUFFER["fg"] = "pink"

def InsertHospInfo():
    global INSERT_BUFFER,Page, YES_BUTTON_BUFFER, NO_BUTTON_BUFFER, SCROLL_BAR, RENDER_TEXT, strOut, MAIN_LABEL_BUFFER

    YES_BUTTON_BUFFER.destroy()
    NO_BUTTON_BUFFER.destroy()

    MAIN_LABEL_BUFFER.destroy()
    SCROLL_BAR.destroy()
    RENDER_TEXT.destroy()

    small_LABEL_BUFFER.destroy()

    Page += 1

    if Page == 4:
        print("")
        print("모든 결과를 열람하셨습니다. ")
        Page = 0
        DeleteInfo()
        return

    else:
        hospQuestion = ENTRY_BUFFER.get()
        print(hospQuestion)

        strOut = getHospitalData(hospQuestion, Page)

        SCROLL_BAR = Scrollbar(g_Tk)
        SCROLL_BAR.pack()
        SCROLL_BAR.place(x=470, y=200)
        TempFont = font.Font(g_Tk, size=10, family='Consolas')
        RENDER_TEXT = Text(g_Tk, width=60, height=40, borderwidth=12, relief='ridge',
                          yscrollcommand=SCROLL_BAR.set)
        RENDER_TEXT.pack()
        RENDER_TEXT.place(x=16, y=165)
        SCROLL_BAR.config(command=RENDER_TEXT.yview)
        SCROLL_BAR.pack(side=RIGHT, fill=BOTH)
        RENDER_TEXT.configure(state='normal')
        RENDER_TEXT.insert(INSERT, strOut)
        RENDER_TEXT["fg"] = "gray"

        #F = lambda bookBuffer, value : bookBuffer + value

        YES_BUTTON_BUFFER = Button(g_Tk,  font=LittleButtonFont, text="Next Page!", command=InsertHospInfo)

        if Page == 3:
            YES_BUTTON_BUFFER.configure(state="disabled")

        YES_BUTTON_BUFFER.pack()
        YES_BUTTON_BUFFER.place(x=320, y=730)
        YES_BUTTON_BUFFER["bg"] = "white"
        YES_BUTTON_BUFFER["fg"] = "pink"

        NO_BUTTON_BUFFER = Button(g_Tk,  font=LittleButtonFont, text="   Quit   ", command=DeleteInfo)
        NO_BUTTON_BUFFER.pack()
        NO_BUTTON_BUFFER.place(x=20, y=730)
        NO_BUTTON_BUFFER["bg"] = "white"
        NO_BUTTON_BUFFER["fg"] = "pink"

        MAIN_LABEL_BUFFER = Label(g_Tk, font=BigButtonFont, text="Hosp")
        MAIN_LABEL_BUFFER.pack()
        MAIN_LABEL_BUFFER.place(x=30, y=45)
        MAIN_LABEL_BUFFER["fg"] = "white"
        MAIN_LABEL_BUFFER["bg"] = "pink"

def FunctionHosp():
    global INSERT_BUFFER, ENTRY_BUFFER, LABEL_BUFFER, INSERT_BUTTON_BUFFER, small_LABEL_BUFFER

    winsound.PlaySound('effect_1.wav', winsound.SND_FILENAME)

    DestoryMenu()

    LABEL_BUFFER = Label(g_Tk, font=ButtonFont , text="About HOSP!")
    LABEL_BUFFER.place(x=120, y=240)
    LABEL_BUFFER["bg"] = "gray"
    LABEL_BUFFER["fg"] = "White"

    small_LABEL_BUFFER = Label(g_Tk, font=LittleLittleButtonFont , text="읍, 면, 동을 입력하세요")
    small_LABEL_BUFFER.place(x=150, y=350)
    small_LABEL_BUFFER["bg"] = "pink"
    small_LABEL_BUFFER["fg"] = "white"

    ENTRY_BUFFER = Entry(g_Tk , font=LittleButtonFont )
    ENTRY_BUFFER.pack()
    ENTRY_BUFFER.place(x=120, y=320)
    ENTRY_BUFFER["fg"] = "gray"

    INSERT_BUTTON_BUFFER = Button(g_Tk, font=LittleLittleButtonFont, text="검색", command = InsertHospInfo)
    INSERT_BUTTON_BUFFER.pack()
    INSERT_BUTTON_BUFFER.place(x=380, y=318)
    INSERT_BUTTON_BUFFER["bg"] = "white"
    INSERT_BUTTON_BUFFER["fg"] = "pink"

def InsertItemInfo():
    global INSERT_BUFFER, Page, YES_BUTTON_BUFFER, NO_BUTTON_BUFFER, SCROLL_BAR, RENDER_TEXT, strOut, isMail, \
        MAIL_BUTTON_BUFFER, isItemImg

    YES_BUTTON_BUFFER.destroy()
    NO_BUTTON_BUFFER.destroy()
    MAIL_BUTTON_BUFFER.destroy()

    MAIN_LABEL_BUFFER.destroy()

    SCROLL_BAR.destroy()
    RENDER_TEXT.destroy()

    small_LABEL_BUFFER.destroy()
    LABEL_BUFFER.destroy()

    Page += 1

    if Page == 4:
        print("")
        print("모든 결과를 열람하셨습니다. ")
        Page = 0
        DeleteInfo()
        return

    else:
        itemQuestion = ENTRY_BUFFER.get()
        print(itemQuestion)

        strOut = getProductData(g_Tk, itemQuestion, Page)

        SCROLL_BAR = Scrollbar(g_Tk)
        SCROLL_BAR.pack()
        SCROLL_BAR.place(x=470, y=200)
        TempFont = font.Font(g_Tk, size=10, family='Consolas')
        RENDER_TEXT = Text(g_Tk, width=60, height=10, borderwidth=12, relief='ridge',
                          yscrollcommand=SCROLL_BAR.set)
        RENDER_TEXT.pack()
        RENDER_TEXT.place(x=16, y=370)
        SCROLL_BAR.config(command=RENDER_TEXT.yview)
        SCROLL_BAR.pack(side=RIGHT, fill=BOTH)
        RENDER_TEXT.configure(state='normal')
        RENDER_TEXT.insert(INSERT, strOut)


        #F = lambda bookBuffer, value : bookBuffer + value

        YES_BUTTON_BUFFER = Button(g_Tk,  font=LittleButtonFont, text="Next!", command=InsertItemInfo)

        if Page == 3:
            YES_BUTTON_BUFFER.configure(state="disabled")

        YES_BUTTON_BUFFER.pack()
        YES_BUTTON_BUFFER.place(x=340, y=730)
        YES_BUTTON_BUFFER["bg"] = "white"
        YES_BUTTON_BUFFER["fg"] = "pink"


        NO_BUTTON_BUFFER = Button(g_Tk,font=LittleButtonFont,text="Quit!",command=DeleteInfo)
        NO_BUTTON_BUFFER.pack()
        NO_BUTTON_BUFFER.place(x=20, y=730)
        NO_BUTTON_BUFFER["bg"] = "white"
        NO_BUTTON_BUFFER["fg"] = "pink"

        isItemImg = True

        isMail = True
        MAIL_BUTTON_BUFFER = Button(g_Tk,  font=LittleButtonFont, text="MAIL!", command=StartMail)
        MAIL_BUTTON_BUFFER.pack()
        MAIL_BUTTON_BUFFER.place(x=220, y=730)
        MAIL_BUTTON_BUFFER["bg"] = "white"
        MAIL_BUTTON_BUFFER["fg"] = "pink"

def FunctionItem():
    global INSERT_BUFFER, ENTRY_BUFFER, LABEL_BUFFER, INSERT_BUTTON_BUFFER, small_LABEL_BUFFER

    winsound.PlaySound('effect_1.wav', winsound.SND_FILENAME)

    DestoryMenu()

    LABEL_BUFFER = Label(g_Tk, font=ButtonFont , text="About ITEM!")
    LABEL_BUFFER.place(x=120, y=240)
    LABEL_BUFFER["bg"] = "gray"
    LABEL_BUFFER["fg"] = "White"

    small_LABEL_BUFFER = Label(g_Tk, font=LittleLittleButtonFont , text="원하는 품목을 입력하세요")
    small_LABEL_BUFFER.place(x=143, y=350)
    small_LABEL_BUFFER["bg"] = "pink"
    small_LABEL_BUFFER["fg"] = "white"

    ENTRY_BUFFER = Entry(g_Tk , font=LittleButtonFont )
    ENTRY_BUFFER.pack()
    ENTRY_BUFFER.place(x=120, y=320)
    ENTRY_BUFFER["fg"] = "gray"

    INSERT_BUTTON_BUFFER = Button(g_Tk, font=LittleLittleButtonFont, text="검색", command = InsertItemInfo)
    INSERT_BUTTON_BUFFER.pack()
    INSERT_BUTTON_BUFFER.place(x=380, y=318)
    INSERT_BUTTON_BUFFER["bg"] = "white"
    INSERT_BUTTON_BUFFER["fg"] = "pink"

def InsertTripInfo():
    global INSERT_BUFFER,Page, YES_BUTTON_BUFFER, NO_BUTTON_BUFFER, SCROLL_BAR, RENDER_TEXT, MAIL_BUTTON_BUFFER, strOut, \
        MAIN_LABEL_BUFFER

    YES_BUTTON_BUFFER.destroy()
    NO_BUTTON_BUFFER.destroy()

    SCROLL_BAR.destroy()
    RENDER_TEXT.destroy()

    MAIN_LABEL_BUFFER.destroy()
    small_LABEL_BUFFER.destroy()

    Page += 1

    if Page == 4:
        print("")
        print("모든 결과를 열람하셨습니다. ")
        Page = 0
        DeleteInfo()
        return

    else:
        tripQuestion = ENTRY_BUFFER.get()
        print(tripQuestion)

        strOut = getTripPlaceDataArea(tripQuestion, Page)

        SCROLL_BAR = Scrollbar(g_Tk)
        SCROLL_BAR.pack()
        SCROLL_BAR.place(x=470, y=200)
        TempFont = font.Font(g_Tk, size=10, family='Consolas')
        RENDER_TEXT = Text(g_Tk, width=60, height=40, borderwidth=12, relief='ridge',
                          yscrollcommand=SCROLL_BAR.set)
        RENDER_TEXT.pack()
        RENDER_TEXT.place(x=16, y=165)
        SCROLL_BAR.config(command=RENDER_TEXT.yview)
        SCROLL_BAR.pack(side=RIGHT, fill=BOTH)
        RENDER_TEXT.configure(state='normal')
        RENDER_TEXT.insert(INSERT, strOut)
        RENDER_TEXT["fg"] = "gray"

        #F = lambda bookBuffer, value : bookBuffer + value

        YES_BUTTON_BUFFER = Button(g_Tk,  font=LittleButtonFont, text="Next Page!", command=InsertTripInfo)

        if Page == 3:
            YES_BUTTON_BUFFER.configure(state="disabled")

        YES_BUTTON_BUFFER.pack()
        YES_BUTTON_BUFFER.place(x=320, y=730)
        YES_BUTTON_BUFFER["bg"] = "white"
        YES_BUTTON_BUFFER["fg"] = "pink"

        NO_BUTTON_BUFFER = Button(g_Tk,  font=LittleButtonFont, text="   Quit   ", command=DeleteInfo)
        NO_BUTTON_BUFFER.pack()
        NO_BUTTON_BUFFER.place(x=20, y=730)
        NO_BUTTON_BUFFER["bg"] = "white"
        NO_BUTTON_BUFFER["fg"] = "pink"

        MAIN_LABEL_BUFFER = Label(g_Tk, font=BigButtonFont, text="TOUR:")
        MAIN_LABEL_BUFFER.pack()
        MAIN_LABEL_BUFFER.place(x=30, y=45)
        MAIN_LABEL_BUFFER["fg"] = "white"
        MAIN_LABEL_BUFFER["bg"] = "pink"

def FunctionTrip():
    global INSERT_BUFFER, ENTRY_BUFFER, LABEL_BUFFER, INSERT_BUTTON_BUFFER, small_LABEL_BUFFER

    winsound.PlaySound('effect_1.wav', winsound.SND_FILENAME)

    DestoryMenu()

    #LABEL_BUFFER = Label(g_Tk, text="원하는 지역을 입력해주세요 1 서울 2 인천 3 대전 4 대구 5광주 6 부산 7 울산 8 세종 : ")

    LABEL_BUFFER = Label(g_Tk, font=ButtonFont , text="About Trip!")
    LABEL_BUFFER.place(x=120, y=240)
    LABEL_BUFFER["bg"] = "gray"
    LABEL_BUFFER["fg"] = "White"

    small_LABEL_BUFFER = Label(g_Tk, font=LittleLittleButtonFont , text="1서울 2인천 3대전 4대구 5광주 6부산 7울산 8세종")
    small_LABEL_BUFFER.place(x=60, y=350)
    small_LABEL_BUFFER["bg"] = "pink"
    small_LABEL_BUFFER["fg"] = "white"

    ENTRY_BUFFER = Entry(g_Tk , font=LittleButtonFont )
    ENTRY_BUFFER.pack()
    ENTRY_BUFFER.place(x=120, y=320)
    ENTRY_BUFFER["fg"] = "gray"

    INSERT_BUTTON_BUFFER = Button(g_Tk, font=LittleLittleButtonFont, text="검색", command = InsertTripInfo)
    INSERT_BUTTON_BUFFER.pack()
    INSERT_BUTTON_BUFFER.place(x=380, y=318)
    INSERT_BUTTON_BUFFER["bg"] = "white"
    INSERT_BUTTON_BUFFER["fg"] = "pink"

bookButton = Button(g_Tk)
hospitalButton = Button(g_Tk)
productButton = Button(g_Tk)
tripplaceButton = Button(g_Tk)

def InitMenu():
    global g_Tk, imageLabel, ButtonFont, bookButton, hospitalButton, productButton, tripplaceButton

    simpleX = 480 / 2 - 25
    simpleY = 500 - 5

    bookButton = Button(g_Tk, font=ButtonFont, text=    "  BOOK  ", command=FunctionBook)
    hospitalButton = Button(g_Tk, font=ButtonFont, text="  HOSP  ", command=FunctionHosp)
    productButton = Button(g_Tk, font=ButtonFont, text= "  ITEM  ", command=FunctionItem)
    tripplaceButton = Button(g_Tk, font=ButtonFont,text="  TOUR  ", command=FunctionTrip)

    bookButton.pack()
    bookButton.place(x=simpleX - 188, y= simpleY + 110)
    bookButton["bg"] = "white"
    bookButton["fg"] = "pink"

    hospitalButton.pack()
    hospitalButton.place(x=simpleX + 28 , y= simpleY + 110)
    hospitalButton["bg"] = "white"
    hospitalButton["fg"] = "pink"

    productButton.pack()
    productButton.place(x=simpleX - 188, y= simpleY + 200)
    productButton["bg"] = "white"
    productButton["fg"] = "pink"

    tripplaceButton.pack()
    tripplaceButton.place(x=simpleX + 28, y= simpleY + 200)
    tripplaceButton["bg"] = "white"
    tripplaceButton["fg"] = "pink"

def DestoryMenu():
    global ButtonFont, bookButton, hospitalButton, productButton, tripplaceButton
    bookButton.destroy()
    hospitalButton.destroy()
    productButton.destroy()
    tripplaceButton.destroy()

def changeImg():
    global iLoad, imageLabel, isAni
    isAni = True
    # while iLoad < 6:
    iLoad += 1
    print(iLoad)
    #
    if iLoad == 1:
        imageLabel.configure(image=photo_1)
        imageLabel.image = photo_1
    elif iLoad == 2:
        imageLabel.configure(image=photo_2)
        imageLabel.image = photo_2
    elif iLoad == 3:
        imageLabel.configure(image=photo_3)
        imageLabel.image = photo_3
    elif iLoad == 4:
        imageLabel.configure(image=photo_4)
        imageLabel.image = photo_4
    elif iLoad == 5:
        imageLabel.configure(image=photo_5)
        imageLabel.image = photo_5
    elif iLoad == 6:
        imageLabel.configure(image=photo_6)
        imageLabel.image = photo_6
    elif iLoad == 7:
        imageLabel.configure(image=photo_7)
        imageLabel.image = photo_7
    elif iLoad == 8:
        imageLabel.configure(image=photo_8)
        imageLabel.image = photo_8
    elif iLoad == 9:
        imageLabel.configure(image=photo_9)
        imageLabel.image = photo_9

def StartAnimation():
    global g_Tk, imageLabel
    imgbutton = Button(g_Tk, text='클릭', command=changeImg)

    imgbutton.pack()
    imgbutton.place(x=200, y=200)

def clock():
    time = datetime.datetime.now().strftime("Time: %H:%M:%S")
    lab.config(text=time)
    #lab['text'] = time
    g_Tk.after(150, clock) # run itself again after 1000 ms

    if isAni:
        changeImg()



def InitTopText():
    TempFont = font.Font(g_Tk, size=20, weight='bold', family = 'Consolas')
    MainText = Label(g_Tk, font = TempFont, text="For My Angel")
    MainText.pack()
    MainText.place(x=0)

def InitSearchListBox():
    global SearchListBox
    #
    ListBoxScrollbar = Scrollbar(g_Tk)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=150, y=50)

    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    SearchListBox = Listbox(g_Tk, font=TempFont, activestyle='none',
                            width=10, height=1, borderwidth=12, relief='ridge',
                            yscrollcommand=ListBoxScrollbar.set)

    SearchListBox.insert(1, "문화")
    SearchListBox.insert(2, "병원")
    SearchListBox.insert(3, "영화")
    SearchListBox.insert(4, "가격")
    SearchListBox.insert(5, "여행")

    SearchListBox.pack()
    SearchListBox.place(x=10, y=50)

    ListBoxScrollbar.config(command=SearchListBox.yview)

def InitInputLabel():
    global InputLabel
    TempFont = font.Font(g_Tk, size=15, weight='bold', family = 'Consolas')
    InputLabel = Entry(g_Tk, font = TempFont, width = 26, borderwidth = 12, relief = 'ridge')
    InputLabel.pack()
    InputLabel.place(x=10, y=105)

def InitSearchButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(g_Tk, font = TempFont, text="검색",  command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=330, y=110)

def SearchButtonAction():
    global SearchListBox

    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    iSearchIndex = SearchListBox.curselection()[0]
    if iSearchIndex == 0:
        SearchLibrary()
    elif iSearchIndex == 1:
        pass#SearchGoodFoodService()
    elif iSearchIndex == 2:
        pass#SearchMarket()
    elif iSearchIndex == 3:
        pass#SearchCultural()

    RenderText.configure(state='disabled')

def SearchLibrary():
    import http.client
    from xml.dom.minidom import parse, parseString
    conn = http.client.HTTPConnection("openAPI.seoul.go.kr:8088")
    conn.request("GET", "/6b4f54647867696c3932474d68794c/xml/GeoInfoLibrary/1/800")
    req = conn.getresponse()

    global DataList
    DataList.clear()

    if req.status == 200:
        BooksDoc = req.read().decode('utf-8')
        if BooksDoc == None:
            print("에러")
        else:
            parseData = parseString(BooksDoc)
            GeoInfoLibrary = parseData.childNodes
            row = GeoInfoLibrary[0].childNodes

            for item in row:
                if item.nodeName == "row":
                    subitems = item.childNodes

                    if subitems[3].firstChild.nodeValue == InputLabel.get():
                        pass
                    elif subitems[5].firstChild.nodeValue == InputLabel.get():
                        pass
                    else:
                        continue

                    if subitems[29].firstChild is not None:
                        tel = str(subitems[29].firstChild.nodeValue)
                        pass
                        if tel[0] is not '0':
                            tel = "02-" + tel
                            pass
                        DataList.append((subitems[15].firstChild.nodeValue, subitems[13].firstChild.nodeValue, tel))
                    else:
                        DataList.append((subitems[15].firstChild.nodeValue, subitems[13].firstChild.nodeValue, "-"))

            for i in range(len(DataList)):
                RenderText.insert(INSERT, "[")
                RenderText.insert(INSERT, i + 1)
                RenderText.insert(INSERT, "] ")
                RenderText.insert(INSERT, "시설명: ")
                RenderText.insert(INSERT, DataList[i][0])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "주소: ")
                RenderText.insert(INSERT, DataList[i][1])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "전화번호: ")
                RenderText.insert(INSERT, DataList[i][2])
                RenderText.insert(INSERT, "\n\n")

def InitRenderText():
    global RenderText

    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375, y=200)

    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk, width=49, height=27, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=10, y=215)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

    RenderText.configure(state='disabled')

#def ThinterUI():

#clock()

InitMenu()
"""
InitTopText()
InitSearchListBox()
InitInputLabel()
InitSearchButton()
InitRenderText()
"""
#InitSendEmailButton()
#InitSortListBox()
#InitSortButton()

g_Tk.mainloop()