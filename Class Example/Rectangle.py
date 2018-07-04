class RectangleClass(object):
    def __init__(self,width,height):
        self.width=width; #Make sure this rectangle has a width variable.
        self.height=height; #Make sure this rectangle has a height variable.

    def get_area(self):
        return (self.width*self.height); #Return the width of the rectangle times the height of the rectangle to get the area.
        #Example. If my width is 3 and my height is 5, the area returned is (3*5)=15;
    
    
