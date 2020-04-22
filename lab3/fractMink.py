import turtle as t

t.speed("slowest")

def draw(l, n):
    x = l / 4 
    
    if n == 0:
        t.forward(x)
        return
    
    
    draw(x,n-1)
    t.left(90)
    draw(x,n-1)

    t.right(90)
    draw(x,n-1)

    t.right(90)
    draw(x,n-1)
    draw(x,n-1)

    t.left(90)
    draw(x,n-1)

    t.left(90)
    draw(x,n-1)
    
    t.right(90)
    draw(x,n-1)

def draw_snow(l,n):
    for i in range (3):
        draw(l,n)
        t.right(120)
    

    



draw(1000, 2)