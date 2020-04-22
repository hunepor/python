import turtle as t
import math
t.speed(500)

def draw(l, n):
    x = math.sqrt(l**2/2)
    
    if n == 0:
        t.forward(x)
        return
    
    t.left(45)
    draw(x, n-1)
    t.right(90)
    draw(x, n-1)
    t.left(45)

def draw_snow(l,n):
    for i in range (3):
        draw(l,n)
        t.right(120)
    

    




draw(500, 9)