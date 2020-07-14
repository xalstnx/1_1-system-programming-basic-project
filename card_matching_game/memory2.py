import random
import tkinter
from tkinter import *
        

class CardDeck:

    def __init__(self,sideLen):
        self.sideLen = sideLen

    def read(self):

        file = open("memory.txt","r")
        line = file.readline()
        self.allWords = []
        while line !="":
            part = line.split("\n")
            self.allWords.append(part[0])
            line = file.readline()
        file.close()

    def random(self):
        random.shuffle(self.allWords)
        self.words = self.allWords[:int(pow(self.sideLen,2)/2)]

    def dubble(self):
        self.words = self.words*2
        random.shuffle(self.words)

    def createCards(self):
        self.cards = []
        for i in self.words:
            self.cards.append(Card(i,False))
        

class Card:

    def __init__(self,word,up):
        self.word = word
        self.up = up

    def __str__(self):
        if self.up == True:
            return self.word
        else:
            return ""

class Application:
    
    def __init__(self, root):
        self.root = root
        self.countClicks = 0
        self.indexToCompare = []
        self.trials = 0
        self.pairs = 0
        self.text = False

        self.root.title("카드 짝맞추기 게임")
        tkinter.Frame(self.root, width=750, height=660, bg="green").pack()

        self.setLevel()

    def setLevel(self):

        self.var = StringVar()
        self.txt = tkinter.Label(self.root, textvariable=self.var).place(x=0, y=0)
        self.var.set("   카드 짝맞추기 게임   ")
                                      
        self.varRadio = IntVar()
        self.bbbuttons=Button(self.root, text="시작", command=self.start)
        self.bbbuttons.pack(anchor = W)

    def start(self):
        self.sideLen = 4 
        self.varRadio.get()

        self.c = CardDeck(self.sideLen)
        OK1 = True
        try:
            self.c.read()
        except IOError:
            text = self.var.get()
            self.var.set("")
            OK1 = False

        if OK1 == True:
            if len(self.c.allWords) < pow(self.sideLen,2)/2:
                text = self.var.get()
                self.var.set("")
            else:
                self.c.random()
                self.c.dubble()
                self.c.createCards()
                self.printBoard()

    def printBoard(self):
        xvar=10
        yvar=70
        self.buttons = []
        cardCount = 0

        #image
        photo=PhotoImage(file="back.png")

        for i in range(self.sideLen):
            for j in range(self.sideLen):

                cmd = lambda index=cardCount: self.click(index)               
                self.buttons.append(tkinter.Button(self.root, command=cmd, text=self.c.cards[cardCount], image=photo))
                self.buttons[cardCount].place(x=xvar, y=yvar)
                self.buttons[cardCount].image=photo

                xvar=xvar+200
                cardCount += 1
            xvar=10
            yvar=yvar+125

        text = self.var.get()
        self.var.set("")
        self.bbbuttons.pack_forget()

    def click(self,index):

        photo1=PhotoImage(file="c1.png")
        photo2=PhotoImage(file="c2.png")
        photo3=PhotoImage(file="c3.png")
        photo4=PhotoImage(file="c4.png")
        photo5=PhotoImage(file="c5.png")
        photo6=PhotoImage(file="c6.png")
        photo7=PhotoImage(file="c7.png")
        photo8=PhotoImage(file="c8.png")

        if self.c.cards[index].up == False:

            self.c.cards[index].up = True
            self.buttons[index].config(text=self.c.cards[index])
            self.countClicks += 1

            #이미지 넣기
            if (self.c.cards[index].word == "1"):
                self.buttons[index].config(text=self.c.cards[index], image=None)
                self.buttons[index].image=None
                self.buttons[index].config(text=self.c.cards[index], image=photo1)
                self.buttons[index].image=photo1

            if (self.c.cards[index].word == "2"):
                self.buttons[index].config(text=self.c.cards[index], image=None)
                self.buttons[index].image=None
                self.buttons[index].config(text=self.c.cards[index], image=photo2)
                self.buttons[index].image=photo2

            if (self.c.cards[index].word == "3"):
                self.buttons[index].config(text=self.c.cards[index], image=None)
                self.buttons[index].image=None
                self.buttons[index].config(text=self.c.cards[index], image=photo3)
                self.buttons[index].image=photo3

            if (self.c.cards[index].word == "4"):
                self.buttons[index].config(text=self.c.cards[index], image=None)
                self.buttons[index].image=None
                self.buttons[index].config(text=self.c.cards[index], image=photo4)
                self.buttons[index].image=photo4

            if (self.c.cards[index].word == "5"):
                self.buttons[index].config(text=self.c.cards[index], image=None)
                self.buttons[index].image=None
                self.buttons[index].config(text=self.c.cards[index], image=photo5)
                self.buttons[index].image=photo5

            if (self.c.cards[index].word == "6"):
                self.buttons[index].config(text=self.c.cards[index], image=None)
                self.buttons[index].image=None
                self.buttons[index].config(text=self.c.cards[index], image=photo6)
                self.buttons[index].image=photo6

            if (self.c.cards[index].word == "7"):
                self.buttons[index].config(text=self.c.cards[index], image=None)
                self.buttons[index].image=None
                self.buttons[index].config(text=self.c.cards[index], image=photo7)
                self.buttons[index].image=photo7

            if (self.c.cards[index].word == "8"):
                self.buttons[index].config(text=self.c.cards[index], image=None)
                self.buttons[index].image=None
                self.buttons[index].config(text=self.c.cards[index], image=photo8)
                self.buttons[index].image=photo8

            if self.text == True:
                text = self.var.get()
                self.var.set("")
                self.text = False

            if len(self.indexToCompare) == 2:
                self.buttons[self.indexToCompare[0]].config(text=self.c.cards[self.indexToCompare[0]])
                self.buttons[self.indexToCompare[1]].config(text=self.c.cards[self.indexToCompare[1]])
                self.indexToCompare = []
                          
            if self.countClicks == 2:
                self.countClicks = 0
                self.indexToCompare.append(index)
                self.compare()
            else:
                self.indexToCompare.append(index)
                self.text = True
                
        else:
            text = self.var.get()
            self.var.set("다시 선택해 주세요.")

    def compare(self):
        photo=PhotoImage(file="back.png")
        #second
        """photo1=PhotoImage(file="c1.png")
        photo2=PhotoImage(file="c2.png")
        photo3=PhotoImage(file="c3.png")
        photo4=PhotoImage(file="c4.png")
        photo5=PhotoImage(file="c5.png")
        photo6=PhotoImage(file="c6.png")
        photo7=PhotoImage(file="c7.png")
        photo8=PhotoImage(file="c8.png")"""

        self.trials += 1

        #image
        """self.c.cards[self.indexToCompare[1]].up = True
        if (self.c.cards[self.indexToCompare[1]].word == "1"):
            self.buttons[self.indexToCompare[1]].config(text=self.c.cards[self.indexToCompare[1]], image=None)
            self.buttons[self.indexToCompare[1]].image=None
            self.buttons[self.indexToCompare[1]].config(text=self.c.cards[self.indexToCompare[1]], image=photo1)
            self.buttons[self.indexToCompare[1]].image=photo1

        if (self.c.cards[self.indexToCompare[1]].word == "2"):
            self.buttons[self.indexToCompare[1]].config(text=self.c.cards[self.indexToCompare[1]], image=None)
            self.buttons[self.indexToCompare[1]].image=None
            self.buttons[self.indexToCompare[1]].config(text=self.c.cards[self.indexToCompare[1]], image=photo2)
            self.buttons[self.indexToCompare[1]].image=photo2

        if (self.c.cards[self.indexToCompare[1]].word == "3"):
            self.buttons[self.indexToCompare[1]].config(text=self.c.cards[self.indexToCompare[1]], image=None)
            self.buttons[self.indexToCompare[1]].image=None
            self.buttons[self.indexToCompare[1]].config(text=self.c.cards[self.indexToCompare[1]], image=photo3)
            self.buttons[self.indexToCompare[1]].image=photo3

        if (self.c.cards[self.indexToCompare[1]].word == "4"):
            self.buttons[self.indexToCompare[1]].config(text=self.c.cards[self.indexToCompare[1]], image=None)
            self.buttons[self.indexToCompare[1]].image=None
            self.buttons[self.indexToCompare[1]].config(text=self.c.cards[self.indexToCompare[1]], image=photo4)
            self.buttons[self.indexToCompare[1]].image=photo4

        if (self.c.cards[self.indexToCompare[1]].word == "5"):
            self.buttons[self.indexToCompare[1]].config(text=self.c.cards[self.indexToCompare[1]], image=None)
            self.buttons[self.indexToCompare[1]].image=None
            self.buttons[self.indexToCompare[1]].config(text=self.c.cards[self.indexToCompare[1]], image=photo5)
            self.buttons[self.indexToCompare[1]].image=photo5

        if (self.c.cards[self.indexToCompare[1]].word == "6"):
            self.buttons[self.indexToCompare[1]].config(text=self.c.cards[self.indexToCompare[1]], image=None)
            self.buttons[self.indexToCompare[1]].image=None
            self.buttons[self.indexToCompare[1]].config(text=self.c.cards[self.indexToCompare[1]], image=photo6)
            self.buttons[self.indexToCompare[1]].image=photo6

        if (self.c.cards[self.indexToCompare[1]].word == "7"):
            self.buttons[self.indexToCompare[1]].config(text=self.c.cards[self.indexToCompare[1]], image=None)
            self.buttons[self.indexToCompare[1]].image=None
            self.buttons[self.indexToCompare[1]].config(text=self.c.cards[self.indexToCompare[1]], image=photo7)
            self.buttons[self.indexToCompare[1]].image=photo7

        if (self.c.cards[self.indexToCompare[1]].word == "8"):
            self.buttons[self.indexToCompare[1]].config(text=self.c.cards[self.indexToCompare[1]], image=None)
            self.buttons[self.indexToCompare[1]].image=None
            self.buttons[self.indexToCompare[1]].config(text=self.c.cards[self.indexToCompare[1]], image=photo8)
            self.buttons[self.indexToCompare[1]].image=photo8"""

        if self.c.cards[self.indexToCompare[0]].word == self.c.cards[self.indexToCompare[1]].word:
            text = self.var.get()
            self.var.set("맞추셨습니다.")
            self.text = True
            
            self.indexToCompare = []
            self.countPairs()
        else:
            self.c.cards[self.indexToCompare[0]].up = False
            self.buttons[self.indexToCompare[0]].config(text=self.c.cards[self.indexToCompare[0]], image=None)
            self.buttons[self.indexToCompare[0]].image=None
            self.buttons[self.indexToCompare[0]].config(text=self.c.cards[self.indexToCompare[0]], image=photo)
            self.buttons[self.indexToCompare[0]].image=photo

            self.c.cards[self.indexToCompare[1]].up = False
            self.buttons[self.indexToCompare[1]].config(text=self.c.cards[self.indexToCompare[1]], image=None)
            self.buttons[self.indexToCompare[1]].image=None
            self.buttons[self.indexToCompare[1]].config(text=self.c.cards[self.indexToCompare[1]], image=photo)
            self.buttons[self.indexToCompare[1]].image=photo

    def countPairs(self):
        self.pairs += 1
        if self.pairs == pow(self.sideLen,2)/2:
            text = self.var.get()
            self.var.set("횟수 "+str(self.trials)+"번 만에 성공")
            self.newGameButton = tkinter.Button(self.root, command=self.newGame, text="다시시작", width="13")
            self.newGameButton.place(x=300, y=600)

    def newGame(self):
        self.newGameButton.destroy()
        for i in range(len(self.buttons)):
            self.buttons[i].destroy()
        self.trials = 0
        self.pairs = 0
        self.text = False
        self.setLevel()


root = tkinter.Tk()
Application(root)
root.mainloop()