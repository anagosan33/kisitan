import sys
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



player1=Player("red   ")
player2=Player("blue  ")
player3=Player("white ")
player4=Player("yellow")
players=[player1,player2,player3,player4]  

while True:
    print("(1:red 2:blue 3:white 4:yellow): ")
    try:
        player_name=int(input()) 
    except ValueError:
        print("########## please select(1~4) ##############")
        continue
    if player_name > 0 and player_name <=4:
        print("(1:+開拓地 2:+都市 3:-都市 4:+メガロ 5:-メガロ 6:+英雄 7:+商人 8:-商人):")
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
            print(player.name+"  points:"+str(player.point)+"　開拓地:"+str(player.kaitakuchi)+"  都市:"+str(player.toshi)+\
                " メガロ:"+str(player.megalopolis)+" 英雄:"+str(player.eiyu)+" 商人:"+str(player.syonin))
        print("   ")
        if players[player_name-1].point >= 13:
            print(players[player_name-1].name +"win")
            sys.exit()
    else :
        print("########## please select(1~4)###########")
    
 




