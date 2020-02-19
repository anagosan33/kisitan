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
        self.calc_point()
    
    def built_megalopolice(self):
        self.megalopolis+=1
        self.calc_point()
    def lost_megalopolice(self):
        self.megalopolis-=1
        self.calc_point()
    
    def get_syonin(self):
        self.syonin+=1
        self.calc_point()
    def lost_syonin(self):
        self.syonin-=1
        self.calc_point()

    def get_eiyu(self):
        self.eiyu+=1
        self.calc_point()
def DeleteEntryValue(event):
  #エントリーの中身を削除
  EditBox.delete(0, tk.END)
root = tk.Tk()
root.title(u"騎士タン点数計算ツール")
root.geometry("400x300")
#label
Static1 = tk.Label(text=u'red')
Static1.pack()
Static1 = tk.Label(text=u'blue')
Static1.pack()
Static1 = tk.Label(text=u'white')
Static1.pack()
Static1 = tk.Label(text=u'yellow')
Static1.pack()
#エントリー
EditBox = tk.Entry()
EditBox.pack()
value = EditBox.get()

player1=Player("red   ")
player2=Player("blue  ")
player3=Player("white ")
player4=Player("yellow")
players=[player1,player2,player3,player4]  

while True:
    print("selct player name:\n 1:red 2:blue 3:white 4:yellow")
    try:
        player_name=int(input()) 
    except ValueError:
        print("########## please select(1~4) ##############")
        continue
    if player_name > 0 and player_name <=4:
        print("selct action:\n 1:builtK 2: builtT 3: lostT 4:builtM 5:lostM 6:getE 7:getS 8:lostS")
        try:
            action=int(input())
        except ValueError:
            print("########## please select(1~4) ##############")
            continue
    
        if action==1:
            players[player_name-1].built_kaitakuci()
        elif action==2: 
             players[player_name-1].built_toshi()
        elif action==3: 
            players[player_name-1].lost_toshi()
        elif action==4: 
            players[player_name-1].built_megalopolice()
        elif action==5: 
            players[player_name-1].lost_megalopolice()
        elif action==6:
            players[player_name-1].get_eiyu()
        elif action==7: 
            players[player_name-1].get_syonin()
        elif action==8: 
            players[player_name-1].lost_syonin()

        for player in players:
            print(player.name+"  points:"+str(player.point)+"　開拓地"+str(player.kaitakuchi)+"  都市:"+str(player.toshi)+\
                " メガロ:"+str(player.megalopolis)+" 英雄:"+str(player.eiyu)+" 商人:"+str(player.syonin))
        
        if players[player_name-1].point >= 13:
            print(players[player_name-1].name +"win")
            sys.exit()
    else :
        print("########## please select(1~4)###########")
    
 




