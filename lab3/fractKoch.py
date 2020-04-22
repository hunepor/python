import turtle as t

t.speed("slowest")

def draw(l, n):
    x = l / 3 
    
    if n == 0:
        t.forward(x)
        return
    
    
    draw(x,n-1)
    t.left(60)
    draw(x,n-1)
    t.right(120)
    draw(x,n-1)
    t.left(60)
    draw(x,n-1)

def draw_snow(l,n):
    for i in range (3):
        draw(l,n)
        t.right(120)
    

    



draw_snow(1000, 1)