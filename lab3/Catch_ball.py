from tkinter import *
from random import randrange as rnd, choice
import time
import math

def playerName():
    """
    Asks for player name.
    """
    global name
    try:
        name = input("Enter the name : ")
    except ValueError:
        name = "Jack"
    return name

#Main Window
root = Tk()
#Size of main window
root.geometry('800x800')
#Main widget - white canvas in main window
canv = Canvas(root, bg="white")
#Expands canvas in both directions
canv.pack(fill=BOTH, expand=1)

l = Label(fg='black', bg='white', width=20)

#Points counter var
points=0
#Colors ball can be 
colors = ['red', 'orange', 'violet', 'green', 'blue']

l.pack()
class Ball:
      
    def __init__(self, widget=None):
        self.widget = widget
        self.r = rnd(30, 50)
        self.x = rnd(self.r, 800 - self.r)
        self.y = rnd(self.r, 800 - self.r)
        self.velx = rnd(-3,3,1)
        self.vely = rnd(-3,3,1)

        self.circle = self.widget.create_oval(self.x - self.r, 
                                self.y - self.r, 
                                self.x + self.r, 
                                self.y + self.r, 
                        fill=choice(colors), width=0)
        
        self.widget.pack()
        self.create()
            
    def create(self):
        self.move()
        self.widget.move(self.circle, self.velx, self.vely)
        self.widget.after(20, self.create)
    
    def move(self):
        if self.x <= self.r or self.x >=800 - self.r:
            self.velx*=-1
        if self.y <= self.r or self.y >=800 - self.r:
            self.vely*=-1
        self.y+=self.vely
        self.x+=self.velx
        return

    def check_coords(self, vel, a):
        if a <= self.r or a >= 800-self.r:
            return vel * -1
        else:
            return vel




def new_ball():
    """
    Creates new ball in window.
    """
    global ball1, ball2
    canv.delete(ALL)
    ball1=Ball(canv)
    ball1.create()
    ball2=Ball(canv)
    ball2.create()
    root.after(6000, new_ball)
    


def click(event):
    """
    Reacts on click in ball.

    """
   
    global points
    hyp1=math.sqrt((event.x-ball1.x)**2 + (event.y-ball1.y)**2)
    hyp2=math.sqrt((event.x-ball2.x)**2 + (event.y-ball2.y)**2)
    if hyp1 < ball1.r or hyp2 < ball2.r:
        points+=1
        l['text']=str(points)
        print("yep")
        return True
        
    else:
        print("nope")
    

def write_to_results():
    """
    Writes result into text file.
    """
    global name
    results=open('.//results.txt', 'a')
    results.write("{}: {}\n".format(playerName(), points))
    results.close()




new_ball()
canv.bind('<Button-1>', click)
mainloop()
#write_to_results()
print("Your points are:", points)

