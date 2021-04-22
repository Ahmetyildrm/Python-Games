import random
import turtle
from turtle import Turtle
import time

## Insert your gifs below
image1 = "ahmet.gif" #image for turtle 1, eklemek için kendi kısmındaki yorum satırını kaldır
image2 = "huseyin.gif" #image for turtle 2, eklemek için kendi kısmındaki yorum satırını kaldır
image3 = "kagan.gif"
image4 = "semih.gif"
image5 = "tahsin.gif"

imagelist = [image1, image2, image3, image4, image5]
random.shuffle(imagelist)
tribun = "tribun.gif" #image for tribun

# Window Setup
window = turtle.Screen()
window.title("KAPLUMBAĞA YARIŞI")
turtle.bgcolor("forestgreen")
turtle.color("white")
turtle.speed(0)
turtle.penup()


# Metre çizgileri
# turtle.goto(-350, 170)
#
# for step in range(14):
#   turtle.color("white")
#   turtle.right(90)
#   for num in range(9):
#     turtle.penup()
#     turtle.forward(18)
#     turtle.pendown()
#     turtle.forward(18)
#   turtle.penup()
#   turtle.forward(26)
#   turtle.color("black")
#   turtle.write(step, align='center')
#   turtle.backward(350)
#   turtle.left(90)
#   turtle.forward(40)

turtle.setpos(-178, -300) #Kaplumbağanın pozisyonu
turtle.write("TURTLE RACE", font=("Arial", 30, "bold"))
turtle.penup()




# Toprak
turtle.setpos(-600, -180)
turtle.color("chocolate")
turtle.begin_fill()
turtle.pendown()
turtle.forward(1300)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(1300)
turtle.right(90)
turtle.forward(300)
turtle.end_fill()


# Finish Line
stamp_size = 20
square_size = 15
finish_line = 200
turtle.color("black")
turtle.shape("square")
turtle.shapesize(square_size / stamp_size)
turtle.penup()

for i in range(11):
    turtle.setpos(finish_line, (155 - (i * square_size * 2 )))
    turtle.stamp()

for j in range(11):
    turtle.setpos(finish_line + square_size, ((155 - square_size) - (j * square_size * 2)))
    turtle.stamp()

turtle.hideturtle()

turtle_tribun = Turtle()
turtle_tribun.penup()
turtle_tribun.setpos(0, 300)  # Kaplumbağanın pozisyonu
window.addshape(tribun)
turtle_tribun.shape(tribun)

turtle.color("white")
turtle.setpos(-178, -300) #Kaplumbağanın pozisyonu
turtle.write("TURTLE RACE", font=("Arial", 30, "bold"))

# Kaplumbağa 1

turtle1 = Turtle()
turtle1.speed(0)
turtle1.color("black")
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-350, 144)
turtle1.pendown()



# add the shape first then set the turtle shape
window.addshape(imagelist[0])
turtle1.shape(imagelist[0])

# Kaplumbağa 2

turtle2 = Turtle()
turtle2.speed(0)
turtle2.color("red")
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-350, 72)
turtle2.pendown()



# add the shape first then set the turtle shape
window.addshape(imagelist[1])
turtle2.shape(imagelist[1])

# Kaplumbağa 3

turtle3 = Turtle()
turtle3.speed(0)
turtle3.color("blue")
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(-350, 0)
turtle3.pendown()

# add the shape first then set the turtle shape
window.addshape(imagelist[2])
turtle3.shape(imagelist[2])

# Kaplumbağa 4

turtle4 = Turtle()
turtle4.speed(0)
turtle4.color("yellow")
turtle4.shape("turtle")
turtle4.penup()
turtle4.goto(-350, -72)
turtle4.pendown()

window.addshape(imagelist[3])
turtle4.shape(imagelist[3])

# Kaplumbağa 5

turtle5 = Turtle()
turtle5.speed(0)
turtle5.color("white")
turtle5.shape("turtle")
turtle5.penup()
turtle5.goto(-350, -144)
turtle5.pendown()

window.addshape(imagelist[4])
turtle5.shape(imagelist[4])


stat_list = []
okuma = open("stats.txt","r")
for row in okuma:
    row = row.strip()
    if row:
        stat_list.append(row)

stat_black = 0
stat_red = 0
stat_blue = 0
stat_yellow = 0
stat_white = 0

for stat in stat_list:
    if stat == "Black Turtle":
        stat_black = stat_black + 1
    if stat == "Red Turtle":
        stat_red = stat_red + 1
    if stat == "Blue Turtle":
        stat_blue = stat_blue + 1
    if stat == "Yellow Turtle":
        stat_yellow = stat_yellow + 1
    if stat == "White Turtle":
        stat_white = stat_white + 1



stats = ["Black Turtle:"+str(stat_black),"Red Turtle:"+str(stat_red),"Blue Turtle:"+str(stat_blue),"Yellow Turtle:"+str(stat_yellow),"White Turtle:"+str(stat_white)]
xpos = -270
turtle.setpos(-410, -245)
turtle.color("purple")
turtle.write("Wins",  font=("Comic Sans MS", 13, "bold"))
for i in stats:
    """
    if "White" in i:
        turtle.color("white")
    if "Black" in i:
        turtle.color("black")
    if "Red" in i:
        turtle.color("red")
    if "Blue" in i:
        turtle.color("blue")
    if "Yellow" in i:
        turtle.color("yellow")
        """
    turtle.color("black")
    turtle.setpos(-450, xpos)  # Kaplumbağanın pozisyonu
    turtle.write(i, font=("Comic Sans MS", 13, "bold"))
    xpos = xpos - 25

turtle.color("white")





time.sleep(1) # Oyunu 1 sn beklet

# Hareket ettir
t1_total = 0
t2_total = 0
t3_total = 0
t4_total = 0
t5_total = 0
for i in range(550):
    t1_move = random.randint(1, 5)
    turtle1.forward(t1_move)
    t1_total = t1_total + t1_move

    t2_move = random.randint(1, 5)
    turtle2.forward(t2_move)
    t2_total = t2_total + t2_move

    t3_move = random.randint(1, 5)
    turtle3.forward(t3_move)
    t3_total = t3_total + t3_move

    t4_move = random.randint(1, 5)
    turtle4.forward(t4_move)
    t4_total = t4_total + t4_move

    t5_move = random.randint(1, 5)
    turtle5.forward(t5_move)
    t5_total = t5_total + t5_move

    if t1_total>530 or t2_total>530 or t3_total>530 or t4_total>530 or t5_total>530:
        kazanan = max(t1_total,t2_total,t3_total,t4_total,t5_total)
        if t1_total > 530:
            turtle.setpos(-155, -240)  # Kaplumbağanın pozisyonu-
            turtle.write("Winner: Black Turtle", font=("Helvetica", 19, "bold"))
            break
        if t2_total > 530:
            turtle.setpos(-155, -240)  # Kaplumbağanın pozisyonu
            turtle.write("Winner: Red Turtle", font=("Helvetica", 19, "bold"))
            break
        if t3_total > 530:
            turtle.setpos(-155, -240)  # Kaplumbağanın pozisyonu
            turtle.write("Winner: Blue Turtle", font=("Helvetica", 19, "bold"))
            break
        if t4_total > 530:
            turtle.setpos(-155, -240)  # Kaplumbağanın pozisyonu
            turtle.write("Winner: Yellow Turtle", font=("Helvetica", 19, "bold"))
            break
        if t5_total > 530:
            turtle.setpos(-155, -240)  # Kaplumbağanın pozisyonu
            turtle.write("Winner: White Turtle", font=("Helvetica", 19, "bold"))
            break


Turtle_names = ["Black Turtle", "Red Turtle", "Blue Turtle", "Yellow Turtle", "White Turtle"]
Turtle_points = [t1_total,t2_total,t3_total,t4_total,t5_total]

for k in range(len(Turtle_points)-1):
    if Turtle_points[k] == Turtle_points[k+1]:
        Turtle_points[k] = Turtle_points[k] - 0.5

print(Turtle_points)
tmp_points = [t1_total,t2_total,t3_total,t4_total,t5_total]
Turtle_points.sort()
Scorboard = []

siratmp = 6

for sira in range(len(Turtle_points)):
    for siralama in range(len(tmp_points)):
        if Turtle_points[sira] == tmp_points[siralama]:
            siratmp -= 1
            print(siratmp,":",Turtle_names[siralama])
            yazi = str(siratmp)+":"+str(Turtle_names[siralama])
            Scorboard.append(yazi)
            if siratmp == 1:
                yazma = open("stats.txt", "a")
                yazma.write(str(Turtle_names[siralama])+"\n")
                yazma.close()

Scorboard.reverse()
print(Scorboard)
xpos = 100
for i in Scorboard:
    turtle.setpos(+265, xpos)  # Kaplumbağanın pozisyonu
    turtle.write(i, font=("Comic Sans MS", 13, "bold"))
    xpos = xpos - 25





print(stat_black)
print(stat_red)
print(stat_blue)
print(stat_yellow)
print(stat_white)

window.mainloop()