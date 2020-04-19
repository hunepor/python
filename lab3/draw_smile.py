from graph import *

windowSize(500,500)

def draw_smile():
    """Drawing smile"""
    draw_face_circle()
    #drawin left eye
    draw_eye(200,200,35,12,"red","black")
    #drawing right eye
    draw_eye(330,200,30,10,"red","black")
    #drawing_mouth
    draw_mouth()
    #drawing brows
    draw_brow(250, 180, 100, 100)
    draw_brow(280, 180, 420, 100)
    run()

def draw_face_circle():
    penColor("black")
    brushColor("yellow")
    circle(250, 250, 150)
    

def draw_eye(x,y,r1,r2,c1,c2):
    
    penColor("black")
    brushColor(c1)
    circle(x,y, r1)
    brushColor(c2)
    circle(x,y, r2)

def draw_mouth():
    brushColor("black")
    rectangle(150, 350, 320, 320)

def draw_brow(x, y, x1, y1):
    penSize(15)
    penColor("black")
    moveTo(x, y)
    lineTo(x1, y1)

draw_smile()