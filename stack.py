import turtle
import random
import sys
sys.setExecutionLimit(80000)

color_list = ["red", "orange", "yellow", "green", "blue"]
num_turtles = 4
distance = 25
t_list = []

for i in range(num_turtles):
    t = turtle.Turtle()
    t_list.append(t) 
    color = random.choice(color_list)
    t_list[i].shape("turtle")
    t_list[i].color(color)
    t_list[i].left(90)
    t_list[i].penup()
    t_list[i].goto(0, -210 + distance)
    t_list[i].pendown()
    distance += 25

for _ in range(3):
        
    new_num_turtles = int(input("How many turtles do you want to add to the stack?: "))


    for i in range(new_num_turtles):
        t = turtle.Turtle()
        t_list.append(t) 
        color = random.choice(color_list)
        t.shape("turtle")
        t.color(color)
        t.penup()
        t.left(90)
        t.goto(0, -210 + distance)
        t.pendown()
        distance += 25

    remove_turtles = int(input("How many turtles do you want to remove?: "))

    if remove_turtles > 0 and remove_turtles <= num_turtles + new_num_turtles:                
        for i in range(remove_turtles):
            x_cor = random.uniform(-300, 300)
            y_cor = random.uniform(250, 300)
            removed_turtle = t_list.pop()
            removed_turtle.penup()
            removed_turtle.goto(x_cor, y_cor)
            distance -= 25

colored_turtle_lists = [[], [], [], [], []]
for turt in t_list:
    color_index = color_list.index(turt.color()[0])
    colored_turtle_lists[color_index].append(turt)
    
x = -40            
for turt_list in colored_turtle_lists:
    distance = 0
    for turt in turt_list:
        turt.penup()
        turt.goto(x, -180 + distance)
        distance += 25
    x += 40
    
