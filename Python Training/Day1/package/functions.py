import math

def circumference(radius):
    return 2*3.14*radius

def area_circle(radius):
    return 3.14*radius*radius



def perimeter_rectangle(length,breadth):
    return (2*(length+breadth))

def area_rectangle(length,breadth):
    return (length*breadth)



def area_parallelogram(base,height):
    return (base*height)

def perimeter_parallelogram(base,side):
    return (2*(base+side))


def area_rhombus (side, theta):
    return(side*side*math.sin(theta))

def perimeter_rhombus(side):
    return(4*side)


def area_triangle(side1,side2,side3):
    s=(side1+side2+side3)/2
    return ((s*(s-side1)*(s-side2)*(s-side3))**0.5)

def perimeter_triangle(side1,side2,side3):
    return (side1+side2+side3)


def area_hexagon(side):
    return ((3*math.sqrt(3)*side*side)/2)

def perimeter_hexagon(side):
    return (6*side)