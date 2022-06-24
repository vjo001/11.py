import turtle
import random

w = 500
h = 500
food_size = 10
delay = 100

offsets = {
    "up": (0, 10),
    "down": (0, -10),
    "left": (-10, 0),
    "right": (10, 0)
}

def reset():
    global snake, snake_dir, food_position, pen
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    snake_dir = "up"
    food_position = get_random_food_position()
    food.goto(food_position)
    move_snake()
    
def move_snake():
    global snake_dir
    
    new_head = snake[-1].copy()
    new_head[0] = snake[-1][0] + offsets[snake_dir][0]
    new_head[1] = snake[-1][1] + offsets[snake_dir][1]
   
    
    if new_head in snake[:-1]:
        reset()
    else:
        snake.append(new_head)
        
        
        if not food_collison():
            snake.pop(0)
            
            
        if snake[-1][0] > w / 2:
            snale[-1][0] -= w
        elif snake[-1][0] < - w / 2:
            snake[-1][0] += w
        elif snake[-1][1] > h / 2:
            snake[-1][1] -= h
        elif snake[-1][1] < -h /2:
            snake[-1][1] += h
            
            
            pen.clearstanps()
            
            
            for segment in snake:
                pen.goto(segment(0), segment(1))
                pen.stamp
                
                
            screen.update()
            
            turtle.ontimer(move_snake, delay)
            
def food_collision():
    global food_position
    if get_distance(snake(-1), food_position) < 20:
        food_position = get_randon_food_position()
        food.goto(food_position)
        return True
    return False

def get_random_food_position():
    x = randon.randint(- w / 2 + food_size, w / 2 - food_size)
    y = randon.randint(- h / 2 + food_size, h / 2 - food_size)
    return(x, y)

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x2) ** 2) ** 0.5
    return distance

def go_up():
    global snake_dir
    if snake dir != "down":
        snake dir = "up"

def go_right():
    global snake_dir
    if snake dir != "left":
        snake dir = "right"

def go_down():
    global snake_dir
    if snake dir != "up":
        snake dir = "down"

def go_left():
    global snake_dir
    if snake dir != "right":
        snake dir = "left"

screen = turtle.Screen()
screen.setup(w, h)
screen.title("Snake")
screen.bgcolor("purple")
screen.setup(500, 500)
screen.tacer(0)


pen = turtle.Turtle("spuare")
pen.penup()


food = turtle.Turtle()
food.shape("square")
food.color("orange")
food.shapesize(food_size / 20)
food.penup()


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")


reset()
turtle.done()