from tkinter import *
from random import*

# def shiftright(realblank):
#    if realblank==0 or 4 or 8 or 12:
#       break
#    else:
#       holder=realblank-1
#       return (holder)
  
master = Tk()

w = Canvas(master, width=400, height=400, bg='cyan')
w.pack()

w.create_line(100, 0, 100, 400)
w.create_line(200, 0, 200, 400)
w.create_line(300, 0, 300, 400)
w.create_line(400, 0, 400, 400)
w.create_line(400, 100, 0, 100)
w.create_line(400, 200, 0, 200)
w.create_line(400, 300, 0, 300)
w.create_line(400, 400, 0, 400)
randomizer=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15," "]
scramble = sample(randomizer, 16)
print(scramble)
a=scramble[0]
b=scramble[1]
c=scramble[2]
d=scramble[3]
e=scramble[4]
f=scramble[5]
g=scramble[6]
h=scramble[7]
i=scramble[8]
j=scramble[9]
k=scramble[10]
l=scramble[11]
m=scramble[12]
n=scramble[13]
o=scramble[14]
p=scramble[15]
blankspace=scramble.index(' ')
realblank=blankspace+1
print (realblank)
w.create_text(50,50,fill="black",font="Times 20 italic bold",text=a)
w.create_text(150,50,fill="black",font="Times 20 italic bold",text=b)
w.create_text(250,50,fill="black",font="Times 20 italic bold",text=c)
w.create_text(350,50,fill="black",font="Times 20 italic bold",text=d)
w.create_text(50,150,fill="black",font="Times 20 italic bold",text=e)
w.create_text(150,150,fill="black",font="Times 20 italic bold",text=f)
w.create_text(250,150,fill="black",font="Times 20 italic bold",text=g)
w.create_text(350,150,fill="black",font="Times 20 italic bold",text=h)
w.create_text(50,250,fill="black",font="Times 20 italic bold",text=i)
w.create_text(150,250,fill="black",font="Times 20 italic bold",text=j)
w.create_text(250,250,fill="black",font="Times 20 italic bold",text=k)
w.create_text(350,250,fill="black",font="Times 20 italic bold",text=l)
w.create_text(50,350,fill="black",font="Times 20 italic bold",text=m)
w.create_text(150,350,fill="black",font="Times 20 italic bold",text=n)
w.create_text(250,350,fill="black",font="Times 20 italic bold",text=o)
w.create_text(350,350,fill="black",font="Times 20 italic bold",text=p)
mainloop()
