# Problem 1
# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
class Line():
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        self.sub_x = self.coor2[0] - self.coor1[0]
        self.sub_y = self.coor2[1] - self.coor1[1]

    def distance(self):
        return (self.sub_x**2 + self.sub_y**2)**(1/2)

    def slope(self):
        return self.sub_y/self.sub_x

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print(li.distance())
print(li.slope())

# Problem 2
# Fill in the class
from math import pi

class Cylinder():
    def __init__(self, height = 1, radius = 1):
        self.height = height
        self.radius = radius
        self.area = pi*(self.radius**2)

    def volume(self):
        return self.area*self.height

    def surface_area(self):
        return 2*self.area + 2*pi*self.radius*self.height

c = Cylinder(2, 3)
print(c.volume())
print(c.surface_area())