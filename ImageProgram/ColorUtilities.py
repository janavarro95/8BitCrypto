#Color Utilities
from Color import Color;
from random import randint;

def randomColor():
    red=randint(0,255);
    green=randint(0,255);
    blue=randint(0,255);
    return Color(red,green,blue,255);
