#Image Utilities
from PIL import Image;
from Color import Color;
import random;


#Notes, the (0,0) position of an image is the upper left hand corner.

def createPNGImage(mode,width,height,Color):
    """
    Create a new png image with the given width, height and color for the whole image.
    """
    return Image.new(mode,(width,height),Color.getColor());

def getPixel(image,x,y):
    """
    Get a pixel at the x, y position of the image.
    """
    pixelData=list(image.getdata());

    w,h=image.size;
    if(x>w):
        print("ERROR: X outside of width of image!");
        return;
    if(y>h):
        print("ERROR: Y outside of height of image!");
        return;
    position=(y*w)+x;
    r,g,b,a=pixelData[position];
    return Color(r,g,b,a);

def getPixelList(image):
    """
    Get a list of all of the pixels in the image. Each pixel has a red, green, blue, alpha value that looks like (255,0,0,255). The numbers corespond to how much color or alpha the pixel has.
    """
    return list(image.getdata());

def getRedFromList(image,pixelData,x,y):
    """
    If given the list of pixels in the image and the position of the pixel in the image, return the red value associated with that pixel.
    """
    w,h=image.size;
    if(x>w):
        print("ERROR: X outside of width of image!");
        return;
    if(y>h):
        print("ERROR: Y outside of height of image!");
        return;
    position=(y*w)+x;
    r,g,b,a=pixelData[position];
    color=Color(r,g,b,a);
    return color.red;

def getGreenFromList(image,pixelData,x,y):
    """
    If given the list of pixels in the image and the position of the pixel in the image, return the green value associated with that pixel.
    """
    w,h=image.size;
    if(x>w):
        print("ERROR: X outside of width of image!");
        return;
    if(y>h):
        print("ERROR: Y outside of height of image!");
        return;
    position=(y*w)+x;
    r,g,b,a=pixelData[position];
    color=Color(r,g,b,a);
    return color.green;

def getBlueFromList(image,pixelData,x,y):
    """
    If given the list of pixels in the image and the position of the pixel in the image, return the blue value associated with that pixel.
    """
    w,h=image.size;
    if(x>w):
        print("ERROR: X outside of width of image!");
        return;
    if(y>h):
        print("ERROR: Y outside of height of image!");
        return;
    position=(y*w)+x;
    r,g,b,a=pixelData[position];
    color=Color(r,g,b,a);
    return color.blue;

def getAlphaFromList(image,pixelData,x,y):
    """
    If given the list of pixels in the image and the position of the pixel in the image, return the alpha value associated with that pixel.
    """
    w,h=image.size;
    if(x>w):
        print("ERROR: X outside of width of image!");
        return;
    if(y>h):
        print("ERROR: Y outside of height of image!");
        return;
    position=(y*w)+x;
    r,g,b,a=pixelData[position];
    color=Color(r,g,b,a);
    return color.alpha;

def cleanImage(image):
    """
    Erases a previously encrypted message in an image by resetting all of the alpha values.
    """
    pixelData=list(image.getdata());
    w,h=image.size;
    size=w*h;
    for x in range(size):
        r=0;
        g=0;
        b=0;
        a=0;
        try:
            r,g,b,a=pixelData[x];
        except:
            r,g,b=pixelData[x];
            a=255;
        a=255
        color=Color(r,g,b,a);
        color.alpha=255;
        pixelData[x]=color.getColor();
    image.putdata(pixelData)

def setPixelAlphasFromInts(image,ints):
    """
    Encrypt the message into the image's alpha values starting in top right.
    """
    cleanImage(image);
    pixelData=list(image.getdata());
    for x in range(len(ints)):
        r=0;
        g=0;
        b=0;
        a=0;
        try:
            r,g,b,a=pixelData[x];
        except:
            r,g,b=pixelData[x];
            a=255;
        color=Color(r,g,b,a);
        color.alpha=ints[x];
        pixelData[x]=color.getColor();
    image.putdata(pixelData)

def setPixelAlphasFromIntsRandom(image,ints):
    """
    Encrypt the message into the image's alpha values starting in a random order.
    """
    cleanImage(image);
    pixelData=list(image.getdata());

    length=len(ints);
    rand=int(len(pixelData)/length);
    print("Random spacing: "+str(rand));
    
    position=0;
    
    randomPosition=[];
    for i in range(length):
        value=random.randint(position,(rand-1)+position);
        randomPosition.append(value);
        position+=value-position;

    for x in range(len(ints)):
        r=0;
        g=0;
        b=0;
        a=0;
        print(randomPosition[x]);
        try:
            r,g,b,a=pixelData[randomPosition[x]];
        except:
            r,g,b=pixelData[randomPosition[x]];
            a=255;
        color=Color(r,g,b,a);
        color.alpha=ints[x];
        pixelData[randomPosition[x]]=color.getColor();
    image.putdata(pixelData)

def getPixelRed(image,x,y):
    """
    Get a given pixel's red value.
    """
    color=getPixel(image,x,y);
    return color.red;

def getPixelGreen(image,x,y):
    """
    Get a given pixel's green value.
    """
    color=getPixel(image,x,y);
    return color.green;

def getPixelBlue(image,x,y):
    """
    Get a given pixel's blue value.
    """
    color=getPixel(image,x,y);
    return color.blue;

def getPixelAlpha(image,x,y):
    """
    Get a given pixel's alpha value.
    """
    color=getPixel(image,x,y);
    return color.alpha;

def setPixel(image,x,y,color):
    """
    Get a given pixel and change the color of it to the color passed in.
    """
    pixelData=list(image.getdata());
    w,h=image.size;
    if(x>w):
        print("ERROR: X outside of width of image!");
        return;
    if(y>h):
        print("ERROR: Y outside of height of image!");
        return;
    position=(y*w)+x;
    pixelData[position]=color.getColor();
    image.putdata(pixelData)

def getImageLength(image):
    """
    Get the number of pixels in the image.
    """
    w,h=image.size;
    length=(w*h);
    return length;

def display(image):
    """
    Show the image in a image viewer program.
    """
    image.show();

def save(image,name):
    """
    Save the image.
    """
    image.save(name);

