from tkinter import *
from tkinter import font

from Book_Internet import *
from Weather_internet import *
from TripPlace_Internet import *
from Hospital_Internet import *
from Product_Internet import *

import datetime
import tkinter.messagebox
g_Tk = Tk()
#g_Tk.geometry("400x600+750+200")
g_Tk.geometry("480x800+700+100")

DataList = []

ButtonFont = font.Font(g_Tk, size=30, weight='bold', family='Consolas') #정식 버튼 글씨체

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

SCROLL_BAR = Scrollbar(g_Tk)
RENDER_TEXT = Text(g_Tk)

LABEL_BUFFER = Label(g_Tk)

imageLabel = Label(g_Tk, image=photo_0)
imageLabel.pack()

lab = Label(g_Tk)       #clock
lab.pack()

Page = 0


def InsertBookInfo():
    global INSERT_BUFFER,Page, YES_BUTTON_BUFFER, NO_BUTTON_BUFFER, SCROLL_BAR, RENDER_TEXT


    YES_BUTTON_BUFFER.destroy()
    NO_BUTTON_BUFFER.destroy()
    SCROLL_BAR.destroy()
    RENDER_TEXT.destroy()

    Page += 1

    bookQuestion = ENTRY_BUFFER.get()
    print(bookQuestion)

    strOut = getBookData(g_Tk, bookQuestion, Page)

    SCROLL_BAR = Scrollbar(g_Tk)
    SCROLL_BAR.pack()
    SCROLL_BAR.place(x=470, y=200)
    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RENDER_TEXT = Text(g_Tk, width=60, height=40, borderwidth=12, relief='ridge',
                      yscrollcommand=SCROLL_BAR.set)
    RENDER_TEXT.pack()
    RENDER_TEXT.place(x=16, y=180)
    SCROLL_BAR.config(command=RENDER_TEXT.yview)
    SCROLL_BAR.pack(side=RIGHT, fill=BOTH)
    RENDER_TEXT.configure(state='normal')
    RENDER_TEXT.insert(INSERT, strOut)

    #F = lambda bookBuffer, value : bookBuffer + value

    BUTTON_BUFFER = Button(g_Tk, text="Next Page!", command=InsertBookInfo)
    BUTTON_BUFFER.pack()
    BUTTON_BUFFER.place(x=250, y=750)

    BUTTON_BUFFER_2 = Button(g_Tk, text="   Quit   ", command=DeleteBookInfo)
    BUTTON_BUFFER_2.pack()
    BUTTON_BUFFER_2.place(x=50, y=750)

    if Page == 4:
        print("")
        print("모든 결과를 열람하셨습니다. ")
        Page = 0
        DeleteBookInfo()
        InitMenu()

def DeleteBookInfo():
    global YES_BUTTON_BUFFER, NO_BUTTON_BUFFER, SCROLL_BAR, RENDER_TEXT, INSERT_BUTTON_BUFFER

    YES_BUTTON_BUFFER.destroy()
    NO_BUTTON_BUFFER.destroy()
    SCROLL_BAR.destroy()
    RENDER_TEXT.destroy()

    ENTRY_BUFFER.destroy()
    LABEL_BUFFER.destroy()
    INSERT_BUTTON_BUFFER.destroy()

    InitMenu()

def FunctionBook():
    global INSERT_BUFFER, ENTRY_BUFFER, LABEL_BUFFER, INSERT_BUTTON_BUFFER

    DestoryMenu()

    LABEL_BUFFER = Label(g_Tk, text="책과 관련된 정보를 입력해주세요 : ")
    LABEL_BUFFER.place(x=50, y=200)

    ENTRY_BUFFER = Entry(g_Tk)
    ENTRY_BUFFER.pack()
    ENTRY_BUFFER.place(x=200, y=200)

    INSERT_BUTTON_BUFFER = Button(g_Tk, font=ButtonFont, text="검색", command = InsertBookInfo)
    INSERT_BUTTON_BUFFER.pack()
    INSERT_BUTTON_BUFFER.place(x=200, y=500)


bookButton = Button(g_Tk)
hospitalButton = Button(g_Tk)
productButton = Button(g_Tk)
tripplaceButton = Button(g_Tk)

def InitMenu():
    global g_Tk, imageLabel, ButtonFont, bookButton, hospitalButton, productButton, tripplaceButton

    simpleX = 480 / 2
    simpleY = 800 / 2

    bookButton = Button(g_Tk, font=ButtonFont, text="BOOK", command=FunctionBook)
    hospitalButton = Button(g_Tk, font=ButtonFont, text="병원", command=FunctionBook)
    productButton = Button(g_Tk, font=ButtonFont, text="가격정보", command=FunctionBook)
    tripplaceButton = Button(g_Tk, font=ButtonFont, text="관광지", command=FunctionBook)

    bookButton.pack()
    bookButton.place(x=simpleX - 200, y= simpleY + 100)
    bookButton["bg"] = "white"
    bookButton["fg"] = "pink"

    hospitalButton.pack()
    hospitalButton.place(x=simpleX + 40, y= simpleY + 100)
    hospitalButton["bg"] = "white"
    hospitalButton["fg"] = "pink"

    productButton.pack()
    productButton.place(x=simpleX - 200, y= simpleY + 250)
    productButton["bg"] = "white"
    productButton["fg"] = "pink"

    tripplaceButton.pack()
    tripplaceButton.place(x=simpleX + 40, y= simpleY + 250)
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

clock()

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