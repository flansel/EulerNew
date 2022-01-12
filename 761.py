"""
# import the turtle modules
import turtle
 
side = 0
rvel = 1
svel = 1
# Start a work Screen
ws = turtle.Screen()
 
# Define a Turtle Instance
runner = turtle.Turtle()
swimmer = turtle.Turtle()

# executing loop 6 times for 6 sides

swimmer.right(60)
swimmer.forward(90)
swimmer.right(30)
runner.forward(45)
side+=45

while not False:
 
    # Move forward by 90 units
    runner.forward(rvel)
    side+=rvel
    # Turn left the turtle by 300 degrees
    if side >= 90:
        runner.left(300)
        runner.forward(side-90)
        side = 0
"""


import math

sw = (0, 0)
rn = (0, math.sqrt(1-(.5**2)))

s = .5 #know when to turn

done = False

def rn_move(runner):


while not done:
    rn = rn_move(rn)
    sw = sw_move(sw, rn)
    
    if is_out(sw) or has_looped(sw):
        done = True




