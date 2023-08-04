import numpy as np
import random as ass
class Playtictac:
    def __init__(self) -> None:
        self.tictac=np.array([["*","*","*"],["*","*","*"],["*","*","*"]])
        self.posins=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    def ai(self):
        winpos=[]
        for i in range(3):
            if self.tictac[i][0]==self.tictac[i][1] and self.tictac[i][2]=="*" and self.tictac[i][0]=="O":
                winpos.append([i,2])
            elif self.tictac[i][0]==self.tictac[i][2] and self.tictac[i][1]=="*" and self.tictac[i][0]=="O":
                winpos.append([i,1])
            elif self.tictac[i][1]==self.tictac[i][2] and self.tictac[i][0]=="*" and self.tictac[i][1]=="O":
                winpos.append([i,0])
            elif self.tictac[0][i]==self.tictac[1][i] and self.tictac[2][i]=="*"  and self.tictac[0][i]=="O":
                winpos.append([2,i])
            elif self.tictac[0][i]==self.tictac[2][i] and self.tictac[1][i]=="*" and self.tictac[0][i]=="O" :
                winpos.append([1,i])
            elif self.tictac[1][i]==self.tictac[2][i] and self.tictac[0][i]=="*" and self.tictac[1][i]=="O" :
                winpos.append([0,i])
            else:
                pass
        if self.tictac[0][0]==self.tictac[1][1] and self.tictac[2][2]=="*"  and self.tictac[0][0]=="O":
            winpos.append([2,2])
        elif self.tictac[0][0]==self.tictac[2][2] and self.tictac[1][1]=="*" and self.tictac[0][0]=="O" :
            winpos.append([1,1])
        elif self.tictac[1][1]==self.tictac[2][2] and self.tictac[0][0]=="*" and self.tictac[1][1]=="O" :
            winpos.append([0,0])
            
        elif self.tictac[0][2]==self.tictac[1][1] and self.tictac[2][0]=="*" and self.tictac[0][2]=="O":
            winpos.append([2,0])
        elif self.tictac[0][2]==self.tictac[2][0] and self.tictac[1][1]=="*"and self.tictac[0][2]=="O":
            winpos.append([1,1])
        elif self.tictac[2][0]==self.tictac[1][1] and self.tictac[0][2]=="*" and self.tictac[2][0]=="O":
            winpos.append([0,2])
        else:
            pass
        rere=[]
        for i in range(3):
            if self.tictac[i][0]==self.tictac[i][1] and self.tictac[i][2]=="*" and self.tictac[i][0]=="X":
                rere.append([i,2])
            elif self.tictac[i][0]==self.tictac[i][2] and self.tictac[i][1]=="*" and self.tictac[i][0]=="X":
                rere.append([i,1])
            elif self.tictac[i][1]==self.tictac[i][2] and self.tictac[i][0]=="*" and self.tictac[i][1]=="X":
                rere.append([i,0])
            elif self.tictac[0][i]==self.tictac[1][i] and self.tictac[2][i]=="*"  and self.tictac[0][i]=="X":
                rere.append([2,i])
            elif self.tictac[0][i]==self.tictac[2][i] and self.tictac[1][i]=="*" and self.tictac[0][i]=="X" :
                rere.append([1,i])
            elif self.tictac[1][i]==self.tictac[2][i] and self.tictac[0][i]=="*" and self.tictac[1][i]=="X" :
                rere.append([0,i])
            else:
                pass
        if self.tictac[0][0]==self.tictac[1][1] and self.tictac[2][2]=="*"  and self.tictac[0][0]=="x":
            rere.append([2,2])
        elif self.tictac[0][0]==self.tictac[2][2] and self.tictac[1][1]=="*" and self.tictac[0][0]=="X" :
            rere.append([1,1])
        elif self.tictac[1][1]==self.tictac[2][2] and self.tictac[0][0]=="*" and self.tictac[1][1]=="x" :
            rere.append([0,0])
            
        elif self.tictac[0][2]==self.tictac[1][1] and self.tictac[2][0]=="*" and self.tictac[0][2]=="X":
            rere.append([2,0])
        elif self.tictac[0][2]==self.tictac[2][0] and self.tictac[1][1]=="*"and self.tictac[0][2]=="X":
            rere.append([1,1])
        elif self.tictac[2][0]==self.tictac[1][1] and self.tictac[0][2]=="*" and self.tictac[2][0]=="x":
            rere.append([0,2])
        else:
            pass
        if len(winpos)!=0:
            pcom=winpos[0]
        elif len(rere)!=0:
            pcom=rere[0]
        else:
            pcom=ass.choice(self.posins)
        self.tictac[pcom[0]][pcom[1]]="O"
        self.posins.remove(pcom)
    def draw(self,pos):
        if self.tictac[pos[0]][pos[1]]!="*":
            return "invalid pos choosen"
        else:
            self.posins.remove(pos)
            self.tictac[pos[0]][pos[1]]="X"
        self.ai()
        return self.tictac
    def checkgameover(self):
        winner=0
        for i in range(3):
            if self.tictac[i][0]==self.tictac[i][1] and self.tictac[i][0]==self.tictac[i][2] and self.tictac[i][0]!="*" :
                winner=self.tictac[i][0]
                return f" winner is {winner}!"
            elif self.tictac[0][i]==self.tictac[1][i] and self.tictac[0][i]==self.tictac[2][i] and self.tictac[0][i]!="*" :
                winner=self.tictac[i][0]
                print(winner)
                return f" winner is {winner}@q"
            else:
                pass
        if self.tictac[0][0]==self.tictac[1][1] and self.tictac[0][0]==self.tictac[2][2] and self.tictac[0][0]!="*" :
            winner=self.tictac[0][0]
        elif self.tictac[0][2]==self.tictac[1][1] and self.tictac[0][2]==self.tictac[2][0] and self.tictac[0][2]!="*":
            winner=self.tictac[0][2]
        else:
            pass
        if winner:
            return f"winner is {winner}"
        else:
            return 0
    def show(self):
        return self.tictac
play=Playtictac()
print(play.show())
com=input("q>quit,s>show,d>draw>>> ")
while com!="q":
    if com=="d":
        print(play.posins)
        posi=str(input("ex:00 for(0,0)>> "))
        posi=[int(posi[0]),int(posi[1])]
        print(play.draw(posi))
        winner=play.checkgameover()
        if winner:
            print(winner)
            break
        else:
            pass
    elif com=="s":
        print(play.show())
    else:
        pass
    if len(play.posins)==0:
        print("its a draw")
        print(play.show())
    else:
        pass
    com=input("q>quit,s>show,d>draw>>> ")


        


    