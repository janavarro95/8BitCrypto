from Color import Color;
import ColorUtilities;

class Colors(object):

    #This is a class that holds a list of colors.
    #To make a new color, name the color and type...
    #yellow=Color(255,255,0,255);
    """
    YOU:
        Define any colors you want here and get their values by calling
        Ex)Colors.red.getColor();
    """
    red=Color(255,0,0,255);
    green=Color(0,255,0,255);
    blue=Color(0,0,255,255);

    white=Color(255,255,255,255);
    black=Color(0,0,0,255);
        
    def __init__(self):
        pass;

    def getRandomColor(self):
        """
        Get a randomly generated color.
        """
        return ColorUtilities.randomColor();
