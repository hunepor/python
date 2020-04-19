"""
Моделирует равномерное движение точки с отражением от стенок.
"""
import graphics as gr

size_x = 400
size_y = 400

window = gr.GraphWin("Model", size_x, size_y)
# Начальное положение шарика
coords = gr.Point(200, 200)
# Скорость
velocity = gr.Point(1, -2)
acceleration = gr.Point(0, 0.1)

circle = gr.Circle(coords, 10)
circle.setFill('red')
circle.draw(window)



def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x, 
                         point_1.y + point_2.y)
    
    return new_point

def sub(point_1, point_2):
    new_point = gr.Point(point_1.x - point_2.x, 
                         point_1.y - point_2.y)
    
    return new_point

"""
def draw_circle(coords):
    circle = gr.Circle(coords, 10)
    circle.setFill('red')

    circle.draw(window)
"""



sun = gr.Circle(gr.Point(400, 400), 50)
sun.setFill('yellow')
sun.draw(window)

def check_coords(coords, velocity):
    if coords.y < 0 or coords.y > size_y:
        velocity.y = -velocity.y
    
    if coords.x < 0 or coords.x > size_x:
        velocity.x = -velocity.x

def update_velocity(velocity, acceleration):
    return add(velocity, acceleration)

def update_acceleration(ball_coords, center_coords):
    diff = sub(ball_coords, center_coords)
    distance_2 = (diff.x ** 2 + diff.y ** 2) ** (3/2)

    G = 2000
    return gr.Point( -diff.x*G/distance_2, -diff.y*G/distance_2)


while True:
    #clear_window()

    acceleration = update_acceleration(coords, gr.Point(400, 400))
    circle.move(velocity.x, velocity.y)
    coords = add(coords, velocity)
    velocity = update_velocity(velocity, acceleration)
    check_coords(coords, velocity)

    gr.time.sleep(0.02)

