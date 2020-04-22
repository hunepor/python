import turtle as t
import math
t.speed(1)

def draw(l, n):
    x = math.sqrt(l**2/2)
    a=1
    if n == 0:
        t.forward(x)
        return
    
    t.right (45*a)
    draw(x, n-1)
    t.left (90*a)
    draw(x, n-1)
    t.left (45*a)
    a*=-1

def draw_snow(l,n):
    for i in range (3):
        draw(l,n)
        t.right(120)
    

    




draw(200, 2)