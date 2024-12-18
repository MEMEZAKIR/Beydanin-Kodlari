import random
import time


class point:
    def __init__(self,your_point,pc_point):
        self.your_point=your_point
        self.pc_point=pc_point
x=point(0,0)
   
    
class game:
    def __init__(self):
        self.loop=True


    def menu(self):
        choice=int(input(" \nfor rock press [1]\n for paper press [2]\n for scissors press [3]\n \n \n \n "))
        return choice

    def I_got_an_idea(self):
        choice=self.menu()
        if x.pc_point-x.your_point==2:
            self.YOU_LOSE()
        
        elif x.your_point-x.pc_point==2:
            self.YOU_WİN()
        else:
            return choice

    def program(self):
        choice=self.I_got_an_idea()
        if choice==1:
            choice="rock"
            print(choice)
            print("vs")

            for i in range(10):
                time.sleep(.3)
                print('.', end='', flush=True)

            self.rock()

        elif choice==2:
            choice="paper"
            print(choice)
            print("vs")

            for i in range(10):
                time.sleep(.3)
                print('.', end='', flush=True)

            self.paper()

        elif choice==3:
            choice="scissors"
            print(choice)
            print("vs")  

            for i in range(10):
                time.sleep(.3)
                print('.', end='', flush=True)
                   
            self.scissors()
        
    def rock(self):
        pc_choice=random.randint(1,4)
        if pc_choice==1:
            print("rock \n\n")
            
            for i in range(3):
                time.sleep(.3)
                print('.', end='', flush=True)

            print("DRAW...          you|{}| computer|{}|\n\n".format(x.your_point,x.pc_point))
        
        elif pc_choice==2:
            print("paper \n\n")
            x.pc_point+=1

            for i in range(3):
                time.sleep(.3)
                print('.', end='', flush=True)

            print("you LOST the round...         you|{}| computer|{}|\n\n".format(x.your_point,x.pc_point))
        
        elif pc_choice==3:
            print("scissors \n\n")
            x.your_point+=1

            for i in range(3):
                time.sleep(.3)
                print('.', end='', flush=True)

            print("you WON the round...         you|{}| computer|{}|\n\n".format(x.your_point,x.pc_point))      
        
        self.program() 

    def paper(self):
        pc_choice=random.randint(1,4)
        if pc_choice==1:
            print(" rock \n\n")
            x.your_point+=1

            for i in range(3):
                time.sleep(.3)
                print('.', end='', flush=True)

            print("you WON the round...         you|{}| computer|{}|\n\n".format(x.your_point,x.pc_point))
        
        elif pc_choice==2:
            print("paper \n\n")

            for i in range(3):
                time.sleep(.3)
                print('.', end='', flush=True)

            print("DRAW...          you|{}| computer|{}|\n\n".format(x.your_point,x.pc_point))
        
        elif pc_choice==3:
            print("scissors \n\n")
            x.pc_point+=1

            for i in range(3):
                time.sleep(.3)
                print('.', end='', flush=True)

            print("you LOST the round...         you|{}| computer|{}|\n\n".format(x.your_point,x.pc_point))
        
        self.program()

    def scissors(self):
        pc_choice=random.randint(1,4)
        if pc_choice==1:
            print("rock \n\n")
            x.pc_point+=1

            for i in range(3):
                time.sleep(.3)
                print('.', end='', flush=True)

            print("you LOST the round...         you|{}| computer|{}|\n\n".format(x.your_point,x.pc_point))
        
        elif pc_choice==2:
            print("paper \n\n")
            x.your_point+=1

            for i in range(3):
                time.sleep(.3)
                print('.', end='', flush=True)

            print("you WON the round...         you|{}| computer|{}|\n\n".format(x.your_point,x.pc_point))
        
        elif pc_choice==3:
            print("scissors \n\n")

            for i in range(3):
                time.sleep(.3)
                print('.', end='', flush=True)

            print("DRAW...          you|{}| computer|{}|\n\n".format(x.your_point,x.pc_point))

        self.program()

    def YOU_LOSE(self):
        print("computer wins... \n\n YOU_LOSE")
        self.loop=False
        exit()
    

    def YOU_WİN(self):
        print("you win... \n\n BEGGİNER'S LUCK")
        self.loop=False
        exit()
    
rock_paper_scissors=game()
while rock_paper_scissors.loop:
    rock_paper_scissors.program()