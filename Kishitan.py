import sys
import tkinter as tk
class Player():
    def __init__(self,name):
        self.name=name
        self.kaitakuchi=1
        self.toshi=1
        self.megalopolis=0
        self.syonin=0
        self.eiyu=0
        self.point=self.kaitakuchi+2*self.toshi
    
    def calc_point(self):
        self.point=self.kaitakuchi+2*self.toshi+2*self.megalopolis+self.syonin+self.eiyu
        return self.point
    
    def built_kaitakuci(self):
        self.kaitakuchi += 1
        self.calc_point()
        
    def built_toshi(self):
        self.toshi+=1
        self.calc_point()
    def lost_toshi(self):
        self.toshi-=1
        if self.toshi<=0:
            self.toshi=0
        self.calc_point()
    
    def built_megalopolice(self):
        self.megalopolis+=1
        self.calc_point()
    def lost_megalopolice(self):
        self.megalopolis-=1
        if self.megalopolis<=0:
            self.megalopolis=0
        self.calc_point()
    
    def get_syonin(self):
        self.syonin+=1
        if self.syonin>=1:
            self.syonin=1
        self.calc_point()
    def lost_syonin(self):
        self.syonin-=1
        if self.syonin<=0:
            self.syonin=0
        self.calc_point()

    def get_eiyu(self):
        self.eiyu+=1
        self.calc_point()

pnumber=0

def change_p1(event):
    global pnumber
    pnumber=0

def change_p2(event):
    global pnumber
    pnumber=1
    
def change_p3(event):
    global pnumber
    pnumber=2
def change_p4(event):
    global pnumber
    pnumber=3

def var_reload():
    vars[pnumber].set("("+players[pnumber].name+")points:"+str(players[pnumber].point)+"  [開拓地:"+str(players[pnumber].kaitakuchi)+"  都市:"+str(players[pnumber].toshi)+\
                " メガロ:"+str(players[pnumber].megalopolis)+" 英雄:"+str(players[pnumber].eiyu)+" 商人:"+str(players[pnumber].syonin)+" ]")

def add_K(event):
    players[pnumber].built_kaitakuci()
    var_reload()
def add_T(event):
    players[pnumber].built_toshi()
    var_reload()
def lost_T(event):
    players[pnumber].lost_toshi()
    var_reload()
def add_M(event):
    players[pnumber].built_megalopolice()
    var_reload()
def lost_M(event):
    players[pnumber].lost_megalopolice()
    var_reload()
def get_E(event):
    players[pnumber].get_eiyu()
    var_reload()
def get_S(event):
    players[pnumber].get_syonin()
    var_reload()
def lost_S(event):
    players[pnumber].lost_syonin()
    var_reload() 

player1=Player("赤")
player2=Player("青")
player3=Player("白")
player4=Player("黄色")
players=[player1,player2,player3,player4] 

root = tk.Tk()
root.title(u"騎士タン点数計算ツール")
root.geometry("500x300")

#player ボタン
Pbtn1= tk.Button(text=u'赤',foreground="#ff0000")
Pbtn1.pack()
Pbtn1.bind("<Button-1>",change_p1)
Pbtn1.place(x=5,y=5)

Pbtn2= tk.Button(text=u'青',foreground="#0000ff")
Pbtn2.bind("<Button-1>",change_p2)
Pbtn2.pack()
Pbtn2.place(x=45,y=5)

Pbtn3= tk.Button(text=u'白')
Pbtn3.pack()
Pbtn3.place(x=85,y=5)
Pbtn3.bind("<Button-1>",change_p3)

Pbtn4= tk.Button(text=u'黄色',foreground="#ffa500")
Pbtn4.pack()
Pbtn4.bind("<Button-1>",change_p4)
Pbtn4.place(x=125,y=5)


#アクションボタン
bbk = tk.Button(text=u'開拓地+')
bbk.bind("<Button-1>",add_K)
bbk.pack()
bbk.place(x=5,y=50)

bbt = tk.Button(text=u'都市+')
bbt.bind("<Button-1>",add_T)
bbt.pack()
bbt.place(x=75,y=50)

blt = tk.Button(text=u'都市-')
blt.bind("<Button-1>",lost_T)
blt.pack()
blt.place(x=125,y=50)

bbm = tk.Button(text=u'メガロ+')
bbm.bind("<Button-1>",add_M)
bbm.pack()
bbm.place(x=195,y=50)


blm = tk.Button(text=u'メガロ-')
blm.bind("<Button-1>",lost_M)
blm.pack()
blm.place(x=245,y=50)

bge = tk.Button(text=u'英雄+')
bge.bind("<Button-1>",get_E)
bge.pack()
bge.place(x=305,y=50)

bgs = tk.Button(text=u'商人+')
bgs.bind("<Button-1>",get_S)
bgs.pack()
bgs.place(x=375,y=50)

bls = tk.Button(text=u'商人-')
bls.bind("<Button-1>",lost_S)
bls.pack()
bls.place(x=425,y=50)

#socre表示
var1 = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.StringVar()
var4 = tk.StringVar()
vars=[var1,var2,var3,var4]


pnumber=0
var_reload()
score1 = tk.Label(root,textvariable=var1)
score1.pack()
score1.place(x=100,y=100)


pnumber=1
var_reload()
score2 = tk.Label(root,textvariable=var2)
score2.pack()
score2.place(x=100,y=130)


pnumber=2
var_reload()
score3 = tk.Label(root,textvariable=var3)
score3.pack()
score3.place(x=100,y=160)


pnumber=3
var_reload()
score4 = tk.Label(root,textvariable=var4)
score4.pack()
score4.place(x=100,y=190)



root.mainloop() 