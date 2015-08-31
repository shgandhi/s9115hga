from swampy.TurtleWorld import *
from swampy.Gui import *
from math import pi, sin

world = TurtleWorld()
bob = Turtle()
print bob

bob.delay = 0.01

def polyline(t, n, length, angle):
	"""Draws lines of given length at given angle"""
	for i in range(n):
		fd(t, length)
		lt(t, angle)

def arc(t, r, angle):
	"""Draws arcs of the given radis and angle"""
	arc_length = 2 * pi * r * angle / 360
	n = int(arc_length / 3) + 1
	step_length = arc_length / n
	step_angle = float(angle) / n
	polyline(t, n, step_length, step_angle)

def petal(t, r, angle):
	"""Draws a single petal at given radius and angle"""
	arc(t, r, angle)
	lt(t, 180 - angle)
	arc(t, r, angle)
	rt(t, 180 - angle)

def custom_flower(petal_len, num_petals):
	"""Draws flowers with non overlapping petals"""
	for i in range(num_petals):
		petal(bob, petal_len, float(360)/num_petals)
		rt(bob, float(360)/num_petals)

def custom_flower_skewed(petal_len, num_petals):
	"""Draws flowers with overlapping petals"""
	custom_flower(petal_len, num_petals/2)
	rt(bob, float(180))
	custom_flower(petal_len, num_petals/2)
	
def polygon(t, length, n):
	"""Draws polygon with n line segments with given length each. t is the turtle"""
	angle = 360.0/n
	polyline(t, n, length, angle)

def poly_with_lines(t, length, n):
	"""Draws a polygon with radius lines given the length and num of sides"""
	polygon(t, length, n)
	angle = 360.0/n
	lt(t, (180 - angle)/2)
	for i in range(n):
		fd(t, float(length)/(2*sin(pi/n)))
		rt(t, 180 - angle)
		fd(t, float(length)/(2*sin(pi/n)))
		lt(t, 180)

while(True):
	shape_dict = {1:"Seven Petal Flower", 2:"Overlapping Petal Flower", 3:"Twenty Petal Flower", 4:"Pentagon", 5:"Hexagon", 6:"Heptagon", 7:"Exit"}
	print shape_dict
	shape_num = input("Enter the shape 'NUMBER' you want to draw:")
	world.clear()

	if shape_num == 1:
		#Flower1
		custom_flower(100, 7) 
	if shape_num == 2:
		#Flower2
		custom_flower_skewed(100, 10)
	if shape_num == 3:
		#Flower3
		custom_flower(300, 20) 
	if shape_num == 4:
		poly_with_lines(bob, 50, 5)

	if shape_num == 5:
		poly_with_lines(bob, 50, 6)

	if shape_num == 6:
		poly_with_lines(bob, 50, 7)

	if shape_num == 7:
		exit()

wait_for_user()