from PIL import Image;
from Color import Color;
from Colors import Colors;
import random;
import ImageUtilities;


def getInput(image):
    """
    Get user input and make sure it isn't longer than the number of pixels in my image
    Params:
        image<Image>: The image to pass in to check it's size.
    """
    length=ImageUtilities.getImageLength(image);
    message=input("Please input a message of: "+str(length)+" or less characters.");
    if(len(message)>length):
        print("Error, too many characters imput!");
        print("Expected: "+str(length)+" characters or less but got: "+str(len(message))+" characters.");
        return;
    return message;

def charToInt(char):
    """
    Converts a char to an int.
    """
    return ord(char);

def stringToInts(string):
    """
    Converts a string to a list of ints.
    """
    ints=[];
    for char in string:
        ints.append(charToInt(char));
    return ints;

def encode(img):
    """
    An encoding function that gets a message from the user and converts each character in that message to an ascii value. It then takes a bunch of pixels from the image and sets the alpha value of each pixel to a corresponding value from our int list.
    """
    msg=getInput(img); #Get User input
    ints=stringToInts(msg); #Convert all characters in the input to their ascii values
    ImageUtilities.setPixelAlphasFromIntsRandom(img,ints); #For every ascii value set a different pixel's alpha value to that ascii value.
    return img;

def decode(img):
    """
    A decoding function that gets all of the alpha values associated with all the pixels in our image which are somewhere between 0-255 and converts that alpha value to a character.
    """
    ints=[];#A list of ints that will contain all of our alpha values.
    width,height=img.size #Get the width and the height of my image.
    size=width*height; #The number of pixels in our image.
    position=0; #The position we are in out list.
    percent=0; #The percent of decoding we have done for our image.
    pixelData=ImageUtilities.getPixelList(img); #Get all of the pixels in the image and put them into a list.
    for y in range(height): #Iterate across the pixels from top to bottom.
        for x in range(width):#Iterate across out image from left to right.
            alpha=ImageUtilities.getAlphaFromList(img,pixelData,x,y); #Referenced the dumped contents
            if(alpha==255): #If the alpha of our pixel is 255....
                position+=1; #Increment our position
                value=int(size/100);#Get a reference for what 1 percent in our image is.
                if(position%value==0): #If we go up 1 percent...
                    percent+=1; #Increment our percent value
                    print("Decode progress: "+str(percent)+" of 100"); #Print what percent we have gone through in our image.
                continue; #I don't want 255 values because that means I reached the end of my message.
            ints.append(alpha); #Get the alpha value and append it to my list of ints.
            position+=1; #Increment the position variable by 1.
            value=int(size/100); #Get a reference for what 1 percent in our image is.
            if(position%value==0): #If we go up 1 percent...
                percent+=1; #Increment out percent value.
                print("Decode progress: "+str(percent)+" of 100"); #Print what percent we have gone through in our image.

    msg=""; #Make an empty string to store our decoded message.
    for value in ints: #Iterate across my list of ints. (For each int in my list...)
        msg+=chr(value); #Convert my int to it's character value and add it back to my message.
    return msg; #Return my message string.



#Start the main CODE!
Colors=Colors(); #Initialize all of our colors.

userInput=input("Would you like to encode(e) or decode(d) a message?");
if(userInput=="e"):
    e_mode=input("Would you like to open(o) or create(c) a new image?");
    if(e_mode=="c"):
        image_name=input("Please enter the name of the image you wish to create. Example) my_image.png");
        img= ImageUtilities.createPNGImage("RGBA",60,30,Colors.white); #Make a white image

        #Encode the image alpha values.
        img=encode(img);

        #Save and display the image.
        ImageUtilities.save(img,image_name); #Save the image 
    if(e_mode=="o"):
        img_name=input("Please enter the name of the image you wish to open. Example) my_image.png");
        img= Image.open(img_name);
        #Encode the image alpha values.
        img=encode(img);

        #Save and display the image.
        ImageUtilities.save(img,img_name); #Save the image 

if(userInput=="d"):
    imgName=input("Please enter the name of the image you wish to decode. Example) my_image.png");
    img= Image.open(imgName);

    #Encode the image alpha values.
    msg=decode(img);
    print(msg);
    
