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
photo_10 = PhotoImage(file="loadImg_10.png")  # 디폴트 이미지 파일
photo_11 = PhotoImage(file="loadImg_11.png")  # 디폴트 이미지 파일
photo_12 = PhotoImage(file="loadImg_12.png")  # 디폴트 이미지 파일
photo_13 = PhotoImage(file="loadImg_13.png")  # 디폴트 이미지 파일
photo_14 = PhotoImage(file="loadImg_14.png")  # 디폴트 이미지 파일
photo_15 = PhotoImage(file="loadImg_15.png")  # 디폴트 이미지 파일
photo_16 = PhotoImage(file="loadImg_16.png")  # 디폴트 이미지 파일
photo_17 = PhotoImage(file="loadImg_17.png")  # 디폴트 이미지 파일
photo_18 = PhotoImage(file="loadImg_18.png")  # 디폴트 이미지 파일
photo_19 = PhotoImage(file="loadImg_19.png")  # 디폴트 이미지 파일
photo_20 = PhotoImage(file="loadImg_20.png")  # 디폴트 이미지 파일
photo_21 = PhotoImage(file="loadImg_21.png")  # 디폴트 이미지 파일
photo_22 = PhotoImage(file="loadImg_22.png")  # 디폴트 이미지 파일
photo_23 = PhotoImage(file="loadImg_23.png")  # 디폴트 이미지 파일
photo_24 = PhotoImage(file="loadImg_24.png")  # 디폴트 이미지 파일
photo_25 = PhotoImage(file="loadImg_25.png")  # 디폴트 이미지 파일
photo_26 = PhotoImage(file="loadImg_26.png")  # 디폴트 이미지 파일
photo_27 = PhotoImage(file="loadImg_27.png")  # 디폴트 이미지 파일
photo_28 = PhotoImage(file="loadImg_28.png")  # 디폴트 이미지 파일
photo_29 = PhotoImage(file="loadImg_29.png")  # 디폴트 이미지 파일
photo_30 = PhotoImage(file="loadImg_30.png")  # 디폴트 이미지 파일
photo_31 = PhotoImage(file="loadImg_31.png")  # 디폴트 이미지 파일
photo_32 = PhotoImage(file="loadImg_32.png")  # 디폴트 이미지 파일
photo_33 = PhotoImage(file="loadImg_33.png")  # 디폴트 이미지 파일
photo_34 = PhotoImage(file="loadImg_34.png")  # 디폴트 이미지 파일
photo_35 = PhotoImage(file="loadImg_35.png")  # 디폴트 이미지 파일
photo_36 = PhotoImage(file="loadImg_36.png")  # 디폴트 이미지 파일
photo_37 = PhotoImage(file="loadImg_37.png")  # 디폴트 이미지 파일
photo_38 = PhotoImage(file="loadImg_38.png")  # 디폴트 이미지 파일
photo_39 = PhotoImage(file="loadImg_39.png")  # 디폴트 이미지 파일
photo_40 = PhotoImage(file="loadImg_40.png")  # 디폴트 이미지 파일
photo_41 = PhotoImage(file="loadImg_41.png")  # 디폴트 이미지 파일
photo_42 = PhotoImage(file="loadImg_42.png")  # 디폴트 이미지 파일
photo_43 = PhotoImage(file="loadImg_43.png")  # 디폴트 이미지 파일
photo_44 = PhotoImage(file="loadImg_44.png")  # 디폴트 이미지 파일

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

WEATHER_IMG_1 = PhotoImage(file="Weather_1.png")
WEATHER_IMG_2 = PhotoImage(file="Weather_2.png")
WEATHER_IMG_3 = PhotoImage(file="Weather_2.png")
WEATHER_IMG_4 = PhotoImage(file="Weather_4.png")

WEATHER_LABEL_BUFFER = Label(g_Tk, image = WEATHER_IMG_1)
#WEATHER_LABEL_BUFFER = Label(g_Tk, image = PhotoImage(file="buffer.png"))
WEATHER_LABEL_BUFFER.pack()

WEATHER_VALUE = getWeatherData()

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
    global iLoad, imageLabel, isAni, WEATHER_LABEL_BUFFER, WEATHER_VALUE
    isAni = True
    # while iLoad < 6:
    iLoad += 1
    #print(iLoad)
    #
    if iLoad == 1:
        imgbutton.destroy()
        winsound.PlaySound('effect_1.wav', winsound.SND_FILENAME)
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
    elif iLoad == 10:
        imageLabel.configure(image=photo_10)
        imageLabel.image = photo_10
    elif iLoad == 11:
        imageLabel.configure(image=photo_11)
        imageLabel.image = photo_11
    elif iLoad == 12:
        imageLabel.configure(image=photo_12)
        imageLabel.image = photo_12
    elif iLoad == 13:
        imageLabel.configure(image=photo_13)
        imageLabel.image = photo_13
    elif iLoad == 14:
        imageLabel.configure(image=photo_14)
        imageLabel.image = photo_14
    elif iLoad == 15:
        imageLabel.configure(image=photo_15)
        imageLabel.image = photo_15
    elif iLoad == 16:
        imageLabel.configure(image=photo_16)
        imageLabel.image = photo_16
    elif iLoad == 17:
        imageLabel.configure(image=photo_17)
        imageLabel.image = photo_17
    elif iLoad == 18:
        imageLabel.configure(image=photo_18)
        imageLabel.image = photo_18
    elif iLoad == 19:
        imageLabel.configure(image=photo_19)
        imageLabel.image = photo_19
    elif iLoad == 20:
        imageLabel.configure(image=photo_20)
        imageLabel.image = photo_20
    elif iLoad == 21:
        imageLabel.configure(image=photo_21)
        imageLabel.image = photo_21
    elif iLoad == 22:
        imageLabel.configure(image=photo_22)
        imageLabel.image = photo_22
    elif iLoad == 23:
        imageLabel.configure(image=photo_23)
        imageLabel.image = photo_23
    elif iLoad == 24:
        imageLabel.configure(image=photo_24)
        imageLabel.image = photo_24
    elif iLoad == 25:
        imageLabel.configure(image=photo_25)
        imageLabel.image = photo_25
    elif iLoad == 26:
        imageLabel.configure(image=photo_26)
        imageLabel.image = photo_26
    elif iLoad == 27:
        imageLabel.configure(image=photo_27)
        imageLabel.image = photo_27
    elif iLoad == 28:
        imageLabel.configure(image=photo_28)
        imageLabel.image = photo_28
    elif iLoad == 29:
        imageLabel.configure(image=photo_29)
        imageLabel.image = photo_29
        InitMenu()

        if WEATHER_VALUE == "1":
            WEATHER_LABEL_BUFFER.configure(image = WEATHER_IMG_1)
            WEATHER_LABEL_BUFFER.image = WEATHER_IMG_1
        elif WEATHER_VALUE == "2":
            WEATHER_LABEL_BUFFER.configure(image = WEATHER_IMG_2)
            WEATHER_LABEL_BUFFER.image = WEATHER_IMG_2
        elif WEATHER_VALUE == "3":
            WEATHER_LABEL_BUFFER.configure(image = WEATHER_IMG_3)
            WEATHER_LABEL_BUFFER.image = WEATHER_IMG_3
        elif WEATHER_VALUE == "4":
            WEATHER_LABEL_BUFFER.configure(image = WEATHER_IMG_4)
            WEATHER_LABEL_BUFFER.image = WEATHER_IMG_4

        print(WEATHER_VALUE)

        WEATHER_LABEL_BUFFER.place(x=361, y=14)

    elif iLoad == 30:
        imageLabel.configure(image=photo_30)
        imageLabel.image = photo_30
    elif iLoad == 31:
        imageLabel.configure(image=photo_31)
        imageLabel.image = photo_31
    elif iLoad == 32:
        imageLabel.configure(image=photo_32)
        imageLabel.image = photo_32
    elif iLoad == 33:
        imageLabel.configure(image=photo_33)
        imageLabel.image = photo_33
    elif iLoad == 34:
        imageLabel.configure(image=photo_34)
        imageLabel.image = photo_34
    elif iLoad == 35:
        imageLabel.configure(image=photo_35)
        imageLabel.image = photo_35
    elif iLoad == 36:
        imageLabel.configure(image=photo_36)
        imageLabel.image = photo_36
    elif iLoad == 37:
        imageLabel.configure(image=photo_37)
        imageLabel.image = photo_37
    elif iLoad == 38:
        imageLabel.configure(image=photo_38)
        imageLabel.image = photo_28
    elif iLoad == 39:
        imageLabel.configure(image=photo_39)
        imageLabel.image = photo_39
    elif iLoad == 40:
        imageLabel.configure(image=photo_40)
        imageLabel.image = photo_40
    elif iLoad == 41:
        imageLabel.configure(image=photo_41)
        imageLabel.image = photo_41
    elif iLoad == 42:
        imageLabel.configure(image=photo_42)
        imageLabel.image = photo_42
    elif iLoad == 43:
        imageLabel.configure(image=photo_43)
        imageLabel.image = photo_43
    elif iLoad == 44:
        imageLabel.configure(image=photo_44)
        imageLabel.image = photo_44

def StartAnimation():
    global g_Tk, imageLabel, imgbutton, WEATHER_VALUE
    imgbutton = Button(g_Tk, font= LittleButtonFont,text='START', command=changeImg)

    imgbutton.pack()
    imgbutton.place(x=200, y=700)
    imgbutton["bg"] = "white"
    imgbutton["fg"] = "pink"


def clock():
    time = datetime.datetime.now().strftime("Time: %H:%M:%S")
    lab.config(text=time)
    #lab['text'] = time
    g_Tk.after(150, clock) # run itself again after 1000 ms

    if isAni:
        changeImg()

#def ThinterUI():

clock()
StartAnimation()
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