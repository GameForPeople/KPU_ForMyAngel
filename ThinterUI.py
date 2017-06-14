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

imageLabel = Label(g_Tk, image=photo_0)
imageLabel.pack()

lab = Label(g_Tk)       #clock
lab.pack()

def clock():
    time = datetime.datetime.now().strftime("Time: %H:%M:%S")
    lab.config(text=time)
    #lab['text'] = time
    g_Tk.after(150, clock) # run itself again after 1000 ms

    if isAni:
        changeImg()

def changeImg():
    global iLoad, imageLabel, isAni

    isAni = True

    #while iLoad < 6:
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

def InitMenu():
    global g_Tk, imageLabel
    simpleX = 480 / 2
    simpleY = 800 / 2

    TempFont = font.Font(g_Tk, size=30, weight='bold', family = 'Consolas')
    bookButton = Button(g_Tk, font = TempFont, text="BOOK",  command=SearchButtonAction)
    bookButton.pack()
    bookButton.place(x=simpleX - 200, y= simpleY + 100)
    bookButton["bg"] = "pink"
    bookButton["fg"] = "white"

    hospitalButton = Button(g_Tk, font = TempFont, text="병원",  command=SearchButtonAction)
    hospitalButton.pack()
    hospitalButton.place(x=simpleX + 40, y= simpleY + 100)
    hospitalButton["bg"] = "white"

    productButton = Button(g_Tk, font = TempFont, text="가격정보",  command=SearchButtonAction)
    productButton.pack()
    productButton.place(x=simpleX - 200, y= simpleY + 250)
    productButton["bg"] = "white"

    tripplaceButton = Button(g_Tk, font = TempFont, text="관광지",  command=SearchButtonAction)
    tripplaceButton.pack()
    tripplaceButton.place(x=simpleX + 40, y= simpleY + 250)
    tripplaceButton["bg"] = "white"
    tripplaceButton["fg"] = "pink"

    imgbutton = Button(g_Tk, text='클릭', command=changeImg)

    imgbutton.pack()
    imgbutton.place(x=200, y=200)

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