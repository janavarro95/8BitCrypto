import math;

class CircleClass(object):
    def __init__(self,radius):
        self.radius=radius;

    def get_area(self):
        """
        Get the area of my circle.
        """
        return( 3.14 * math.pow(self.radius,2)); #Pi * r^2;
