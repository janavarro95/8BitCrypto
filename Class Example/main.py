from Rectangle import RectangleClass;
from Circle import CircleClass;

rect=RectangleClass(3,5); #Create a new rectangle with width 3, height 5.

area=rect.get_area(); #Get the area of my rect function.

circle=CircleClass(2); #Make a circle with a radius of 2!

circle_area=circle.get_area(); #Get the area of my circle.

rect_2=RectangleClass(5,9); #Make a new rectangle with width 5, and height 9.

circle_2=CircleClass(7);

print("The area of my rectangle is! "+str(area)); #Print the area of my rectangle.

print("The area of my circle is! "+str(circle_area)); #Print the area of my circle.

print("The area of my second rectangle is! "+str(rect_2.get_area())); #Print the area of my second rectangle.

print("The area of my second circle is! "+str(circle_2.get_area())); #Print the area of my second circle.
