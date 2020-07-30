import random 
class guessnumber:
    def check(self,uv,rv):
        if rv=uv:
            print("Grate! Your guess is correct")
        else:
            print("Oo so sad! Your guess is wrong")
gn=guessnumber()
rv=random.randint(0,20)#random value
uv=int(input("enter any number between 0 to 20")) #user value
if uv<20:
    gn.check(rv,uv)
else:
    print("invalid input")