#update
# basically sorted out issue number 2 whilst issue one still remains
# oddly enough if you just put coins on the last level, it will function
# but once you put coins on one level and then go down to another with coins
#then it states  'Coin' object is not callable,


import turtle
import math
import random

wn= turtle.Screen()
wn.bgcolor("black")
wn.title("dungeon game ")
wn.setup(700,700)
wn.tracer(0)

#images=["wall.gif","ork.gif","hero.gif","left.gif","right.gif","gold.gif"]
#for image in images:
#    turtle.register_shape(image)




class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0


    def go_up(self):

        move_to_x = self.xcor()
        move_to_y = self.ycor()+24



        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)


    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor()-24


        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = self.xcor()-24
        move_to_y = self.ycor()


        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = player.xcor()+24
        move_to_y = player.ycor()



        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)


    def is_collision(self,other):
        a = self.xcor()- other.xcor()
        b = self.ycor()- other.ycor()
        distance = math.sqrt ((a ** 2)+(b ** 2) )

        if distance < 5:
            return True
        else:
            return False


class Coin(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold= 100
        self.goto(x,y)

    def destroy(self):
        self.goto(1998,1998)
        self.hideturtle()

class Door(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("purple")
        self.penup()
        self.speed(0)
        self.gold= 100
        self.goto(x,y)

    def destroy(self):
        self.goto(1999,1999)
        self.hideturtle()

class Enemy(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold= 25
        self.goto(x,y)
        self.direction=random.choice(["up","down","left","right"])

    def move(self):
        if self.direction =="up":
            dx= 0
            dy= 24

        elif self.direction =="down":
            dx= 0
            dy= -24

        elif self.direction =="left":
            dx= -24
            dy= 0

        elif self.direction =="right":
            dx= 24
            dy= 0

        else:
            dx = 0
            dy = 0

        if self.is_close(player):
            if player.xcor()<self.xcor():
                self.direction="left"

            elif player.xcor()<self.xcor():
                self.direction="right"

            elif player.ycor()<self.ycor():
                self.direction="down"

            elif player.ycor()<self.ycor():
                self.direction="up"


        # Calculate the spot to move to
        move_to_x = self.xcor()+ dx
        move_to_y = self.ycor()+ dy

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            self.direction=random.choice(["up","down","left", "right"])

        turtle.ontimer(self.move,t=random.randint(100,300))


    def is_close(self,other):
        a = self.xcor()- other.xcor()
        b = self.ycor()- other.ycor()
        distance = math.sqrt ((a ** 2)+(b ** 2) )

        if distance < 75:
            return True
        else:
            return False


    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

enemies =[]
coins =[]
doors =[]

levels = [""]

level_1 =[

"XXXXXXXXXXXXXXXXXXXXXXXXX",
"X XXXXXXX          XXXXXX",
"X XXXXXXX      XX  XXXXXX",
"X  P   XX  E   XX  XXXXXX",
"X      XX      XX    XXXX",
"XXXXX  XX XXX  XXX  XXXXX",
"XXXXXD XX XXX  XXX  XXXXX",
"XXXXX  XX XXX  XXX  XXXXX",
"XXXXX     XXX  XXX  XXXXX",
"XXXXX   E XXX  XXX  XXXXX",
"XXXXX     XXX  XXXXXXXXXX",
"XXXXXXXXX  XX          XX",
"XXXXXXX    XX           X",
"XXXXXXXX  XXXXXXXXXXXXX X",
"XXX        E        XXX X",
"XXX                 XXX X",
"XXX  XXXXXXXXXXXX   XXX X",
"XXX  XX   XXXXXXX   XXXXX",
"XXX  XX   XXXXXXX   XXXXX",
"XXX  XX   XXX     XXXXXXX",
"X    XX XXXXX     XXXXXXX",
"X    XX XXXXXXXX  XXXXXXX",
"X       XXXXXXX   XXXXXXX",
"XXX     XXXXXXXX  XXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
    ]


level_2 =[

"XXXXXXXXXXXXXXXXXXXXXXXXX",
"X XXXXXXX          XXXXXX",
"X XXXXXXX      XX  XXXXXX",
"X  P   XX      XX  XXXXXX",
"X      XX      XX    XXXX",
"XXXXX  XX XXX  XXX  XXXXX",
"XXXXX  XX XXX  XXX  XXXXX",
"XXXXX  XX XXX  XXX  XXXXX",
"XXXXX     XXX  XXX  XXXXX",
"XXXXX     XXX  XXX  XXXXX",
"XXXXX     XXX  XXXXXXXXXX",
"XXXXXXXXX  XX          XX",
"XXXXXXX    XX           X",
"XXXXXXXX  XXXXXXXXXXXXX X",
"XXX            D    XXX X",
"XXX                 XXX X",
"XXX  XXXXXXXXXXXX   XXX X",
"XXX  XX   XXXXXXX   XXXXX",
"XXX  XX E  XXXXXXX  XXXXX",
"XXX  XX   XXX     XXXXXXX",
"X    XXXXXXXX     XXXXXXX",
"X    XX XXXXXXXX  XXXXXXX",
"X       XXXXXXX   XXXXXXX",
"XXX     XXXXXXXX  XXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
    ]


level_3 =[

"XXXXXXXXXXXXXXXXXXXXXXXXX",
"X XXXXXXX          XXXXXX",
"X XXXXXXX      XX  XXXXXX",
"X  P   XX      XX  XXXXXX",
"X      XX      XX    XXXX",
"XXXXX  XX XXX  XXX  XXXXX",
"XXXXX  XX XXX  XXX  XXXXX",
"XXXXX  XX XXX  XXX  XXXXX",
"XXXXX     XXX  XXX  XXXXX",
"XXXXX   D XXX  XXX  XXXXX",
"XXXXX     XXX  XXXXXXXXXX",
"XXXXXXXXXXXXX    E     XX",
"XXXXXXX    XX           X",
"XXXXXXXX  XXXXXXXXXXXXX X",
"XXX          X      XXX X",
"XXX        XXXXXX   XXX X",
"XXX  XXXXXXXXXXXX   XXX X",
"XXX  XX   XXXXXXX   XXXXX",
"XXX  XX E  XXXXXXX  XXXXX",
"XXX  XX   XXX     XXXXXXX",
"X    XXXXXXXX     XXXXXXX",
"X    XX XXXXXXXX  XXXXXXX",
"X       XXXXXXX   XXXXXXX",
"XXX     XXXXXXXX  XXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
    ]

level_4 =[

"XXXXXXXXXXXXXXXXXXXXXXXXX",
"X XXXXXXX          XXXXXX",
"X XXXXXXX      XX  XXXXXX",
"X  P   XX      XX  XXXXXX",
"X      XX      XX    XXXX",
"XXXXX  CC XXX  XXX  XXXXX",
"XXXXX  CC XXX  XXX  XXXXX",
"XXXXX  CC XXX  XXX  XXXXX",
"XXXXX  CCC     XXX  XXXXX",
"XXXXX  C  XXX  XXX  XXXXX",
"XXXXX     XXX  XXXXXXXXXX",
"XXXXXXXX XXXX    E     XX",
"XXXXXXX    XX           X",
"XXXXXXXX  XXXXXXXXXXXXX X",
"XXX                 XXX X",
"XXX        XXXXXX   XXX X",
"XXX  XXXXXXXXXXXX   XXX X",
"XXX  XX   XXXXXXX   XXXXX",
"XXX  XX E  XXXXXX   XXXXX",
"XXX  XX   XXX     XXXXXXX",
"X    XXXXXXXX  C  XXXXXXX",
"X    XX XXXXXXXX  XXXXXXX",
"X       XXXXXXX   XXXXXXX",
"XXX     XXXXXXXX  XXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
    ]



levels.append(level_1)
levels.append(level_2)
levels.append(level_3)
levels.append(level_4)

#row are y ( up/down) column are x (left and right )
#

def setup_maze(level):
    for y in range (len(level)): #tell how many rows there is
        for x in range(len(level[y])): # acquire every x of the y row
            #Get the character at each x,y coordinate
            #NOTE the order of Y AND X in the next line
            character = level [y][x]
            #Calculate the screen x,y coordinates.  Furtherest left upper corner is (0,0)
            screen_x = -288 + (x*24)
            screen_y = 288 - (y*24)

            #check if it is an x ) represent a wall
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.shape("square")
                pen.color("grey")
                pen.stamp()
                walls.append((screen_x,screen_y))

            if character == "P":   # p= player
                player.goto(screen_x, screen_y)

            if character == "C" :
                coins.append(Coin(screen_x, screen_y))

            if character =="E":
                enemies.append(Enemy(screen_x, screen_y))

            if character =="D":
                doors.append(Door(screen_x, screen_y))

pen=Pen()
player= Player()

walls=[]


setup_maze(levels[1])
maze=("level1")

#keyboard binding

turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")



for enemy in enemies:
    turtle.ontimer(enemy.move,t=250)


while True:

    for coin in coins:
        if player.is_collision(coin):
            player.gold += coin.gold
            print("Player Gold: {}".format (player.gold))
            coin.destroy()
            coins.remove(coin)

    for enemy in enemies:
        if player.is_collision(enemy):
            print("Player dies ")

    for door in doors:
        if player.is_collision(door):
            walls.clear()
            pen.clear()
            for enemy in enemies:
                Enemy.destroy(enemy)
            for coin in coins:
                Enemy.destroy(coin)
            for door in doors:
                Door.destroy(door)

            if maze==("level1"):

                setup_maze(levels[2])
                maze=("level2")
            elif maze ==("level2"):
                setup_maze(levels[3])
                maze=("level3")
            else:
                setup_maze(levels[4])

            for enemy in enemies:
                turtle.ontimer(enemy.move,t=250)

    wn.update()