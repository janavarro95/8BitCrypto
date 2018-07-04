class Color(object):

    def __init__(self,r,g,b,a):
        """
        Define a new color to use.
        Params:
            Red<int>:The amount of red to use 0-255;
            Green<int>:The amount of green to use 0-255;
            Blue<int>:The amount of blue to use 0-255;
            Alpha<int>:How transparent the image is. 0 is invisible, 255 is completely visible.      
        """
        self.red=r;
        self.green=g;
        self.blue=b;
        self.alpha=a;

    def __str__(self):
        """
        Define a custom way our color is displayed when we print it.
        """
        return str(self.getColor());


    def getColor(self):
        """
        Returns the tuple representation of the color. Needed for the PIL (Python Imaging Library).
        """
        return (self.red,self.green,self.blue,self.alpha);

    def invert(self):
        """
        Returns the inverted color of the current color.
        """
        red=abs(255-self.red);
        green=abs(255-self.green);
        blue=abs(255-self.blue);
        return Color(red,green,blue,self.alpha);

    
    def addColor(self,color,loop):
        """
        Adds a color to the current color and returns a new color.
        Params:
            color<Color>: The color to add to this color.
            loop<bool>: If the color wraps around or goes towards white.
        """
        red=self.red+color.red;
        green=self.green+color.green;
        blue=self.blue=color.blue;
        alpha=self.alpha+color.alpha;

        if(loop):
            red=red%256;
            green=green%256;
            blue=blue%256;
            alpha=alpha%256;
            return Color(red,green,blue,alpha);
        else:
            if(red>255):
                red=255;
            if(green>255):
                green=255;
            if(blue>255):
                blue=255;
            if(alpha>255):
                alpha=255;
            return Color(red,green,blue,alpha);

    def addRed(self,red,loop):
        """
        Adds more red to the color.
        """
        r=self.red+red;
        if(loop):
            r=r%256;
        else:
            if(r>255):
                r=255;
        return Color(r,self.green,self.blue,self.alpha);

    def addGreen(self,green,loop):
        """
        Adds more green to the color.
        """
        g=self.green+green;
        if(loop):
            g=g%256;
        else:
            if(g>255):
                g=255;
        return Color(self.red,g,self.blue,self.alpha);

    def addBlue(self,blue,loop):
        """
        Adds more blue to the color.
        """
        b=self.blue+blue;
        if(loop):
            b=b%256;
        else:
            if(b>255):
                b=255;
        return Color(self.red,self.green,b,self.alpha);

    def addAlpha(self,alpha,loop):
        """
        Adds more alpha to the color.
        """
        a=self.alpha+a;
        if(loop):
            a=a%256;
        else:
            if(a>255):
                a=255;
        return Color(self.red,self.green,self.blue,a);
