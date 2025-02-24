#snake game by jasper

import turtle
import time
import random

delay = 0.1

score = 0
high_score = 0

#set up the screen
wn = turtle.Screen()
wn.title("Ahas ni Jasper")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #turns off screen updates

# Register the image
wn.register_shape("my face.gif") 
wn.register_shape("chicken.gif")
wn.register_shape("abs.gif")

#snake head
head= turtle.Turtle()
head.speed(0)
head.shape("my face.gif")
head.color("blue")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Snake food
food= turtle.Turtle()
food.speed(0)
food.shape("chicken.gif")
food.color("red")
food.penup()
food.goto(random.randint(-380,380),random.randint(-280,280))

segments =  []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

#Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move(): 
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
        
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
        
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
        
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")  
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

#Main Game loop
while True:
    wn.update()
    
    #Check for a collision with the border 
    if head.xcor() > 380 or head.xcor() < -380 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        
        #Hide the segments
        for segment in segments:
            segment.goto(1000,1000)
            
        #clear the segments list
        segments.clear()
        
        #reset the score
        score = 0
        
        #reset the delay
        delay = 0.1
        
        #Update the score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format (score, high_score), align = "center", font=("Courier", 24, "normal"))
    
    #Check for a collision with the food
    
    if head.distance(food) < 20:
            #move food to a random place on the screen 
            x = random.randint(-390,390)
            y = random.randint(-290,290)
            food.goto(x,y)

            #add a segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("abs.gif")
            new_segment.color("blue")
            new_segment.penup()
            segments.append(new_segment)
            
            #shorten the delay
            delay -= 0.001
            
            #add score
            score += 10
            
            if score > high_score:
                high_score = score
                
            pen.clear()
            pen.write("Score: {}  High Score: {}".format (score, high_score), align = "center", font=("Courier", 24, "normal"))
            
    #move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x,y)
        
    #move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)    
    
    move()
    
    #check for collision with the body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
            #hide the segments
            for segment in segments:
                segment.goto(1000,1000)
                
            #clear the segments
            segments.clear()
            
            #reset the score
            score = 0
            
            #reset the delay
            delay = 0.1
            
            #Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format (score, high_score), align = "center", font=("Courier", 24, "normal"))
    time.sleep(delay)
wn.mainloop()