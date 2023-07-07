import turtle
import random


size = 30
n = 15
window_size= size*n

class rect:
    def __init__(self, x, y ,up, left, down, right):
        self.x = x
        self.y = y
        self.lines = [up,right,down,left]

def buildmaze(n):
    maze = []
    for y in range(n):
        temp = []
        for x in range(n):
            temp = temp + [ rect(x,y,True,True,True,True) ]
        maze = maze + [temp]
    return maze

def draw(obj):
    x = obj.x
    y = obj.y
    curser.up()
    #find the top right corner depending on window_size
    #from that point draw the maze
    curser.goto( x*size - (window_size/2) , (-1*y*size) + (window_size/2))
    for line in obj.lines:
        if line == True:
            curser.color("White")
        if line == False:
            curser.color("Black")
        curser.down()
        curser.forward(1*size)
        curser.right(90)
        
#draw the gitter
def init_maze_draw(maze):
    for y in range(len(maze)):
        for x in range(len(maze)):
            curser.speed(0)
            draw(maze[y][x])
    curser.speed(0)

#init the turtle drawing
def init_curser():
    curser = turtle.Turtle()
    sc = turtle.Screen() 
    sc.setup(window_size,window_size) 
    sc.bgcolor("black") 
    curser.pencolor("white") 
    curser.ht()
    return curser

#returns all rooms reachable rooms which have not been visited yet
def return_free_neighboors(obj,maze):
    x = obj.x
    y = obj.y
    free_neighboors = []

    #up
    if y-1 >= 0:
        if (obj.lines[0] == True):
            free_neighboors = free_neighboors + [(maze[y-1][x],0)]

    #right
    if x+1 < n:
        if (obj.lines[1] == True):
            free_neighboors = free_neighboors + [(maze[y][x+1],1)] 

    #down
    if y+1 <n:
        if (obj.lines[2]  == True):
            free_neighboors = free_neighboors + [(maze[y+1][x],2)]

    #left
    if x-1 >= 0:
        if (obj.lines[3] == True):
            free_neighboors = free_neighboors + [(maze[y][x-1],3)]

    return free_neighboors

def update_room(obj,next_obj, direction):
    #updates the rect lines on the new visited room and the current position
    #direction+2 mod 4 works for new_position. (eg. up will be down for new_position)
    obj.lines[direction] = False
    next_obj.lines[(direction+2)%4] = False

#works like depth first search

def depth_first_search (maze):
    current = maze[0][0]
    stack = []

    #ends if bottom right has been discovered
    while (current.x,current.y) != (n-1,n-1):

        #looks for free neighboors / if there is a room next to the current room which hase not been exploren yet
        #if there is none, go back to the last room which still hase neighboors / stack.pop
        free_neighboors = return_free_neighboors(current,maze)
        if free_neighboors == []:
            current = stack.pop()


        else:
            #random pick a free_neighboor
            free_neighboor = random.choice(free_neighboors)
            next_obj = free_neighboor[0]
            direction = free_neighboor[1]
            #update the rooms / delete the path(wall) we took
            update_room(current ,next_obj, direction)
            #draw the new room
            draw(current)
            #go to the next room and append the current room to the stack for later
            stack.append(current)
            current = next_obj
            

####main###
curser = init_curser()
turtle.shape("turtle")
maze = buildmaze(n)
init_maze_draw(maze)

depth_first_search(maze)

turtle.done()

