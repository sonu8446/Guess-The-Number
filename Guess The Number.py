import random 
class guessnumber:
    def __init__(self,rv,uv):
        self.uv=uv
        self.rv=rv
    def check(self):
        if self.rv==self.uv:
            print("Grate! Your guess is correct")
        else:
            print("Oo so sad! Your guess is wrong")
            print("You should have entered",rv)


rv=random.randint(0,20)#random value
uv=int(input("enter any number between 0 to 20")) #user value
gn=guessnumber(rv,uv)
if uv<20:
    gn.check()
else:
    print("invalid input")
