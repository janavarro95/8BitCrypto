import random;
import path; #User defined library to assist in doing C# Path functionality.


"""YOU: Are not allowed to edit/modify/hack/cheat your way around this file whatsoever.
You may look at it for reference as an idea for what is happening but you can't change anything here.
"""
class Virus(object):

    def __init__(self,Dir,MAX_NUMBER_OF_LINES,MAX_NUMBER_OF_FILES,MODE):
    
        #Constant variables.
        self.MAX_NUMBER_OF_LINES=100;
        self.MAX_NUMBER_OF_FILES=100;
        self.DEBUG=False; #Used to print debug messages to help figure out where to look.
        self.dir=Dir;
        self.MODE=MODE;


    def CreateVirus(self):
        """
        Create a basic virus program that writes a line in the file saying if it is a virus. Otherwise write that it is not a virus.
        """
        #Set up different paths for folders and files.
        basePath=path.getWorkingDirectory();
        virusPath=path.combine(basePath,self.dir);
        path.createDirectory(virusPath);

        #Get random virus position 1 to MAX_NUMBER_OF_LINES
        virusFilePosition=random.randint(1,self.MAX_NUMBER_OF_FILES);

        if(self.DEBUG):
            print("WRITE VIRUS IN FILE: "+str(virusFilePosition));

        for x in range(1,self.MAX_NUMBER_OF_FILES+1):
            #Create all of my files.
            fileName=("File"+str(x)+".txt");
            filePath=path.combine(virusPath,fileName);
            file=open(filePath,"w");
            numOfLines=random.randint(1,self.MAX_NUMBER_OF_LINES); #Get a random line length for the file from 1-100;
            virusLinePosition=random.randint(1,numOfLines); #Get a virus line position between line 1 and the end of the file.
            if(x==virusFilePosition):
                if(self.DEBUG):
                    print("VIRUS LINE POSITION: "+str(virusLinePosition));
            for line in range(1,numOfLines+1):
                #Virus writing logic.
                if(self.MODE==0):
                    self.BasicVirus(file,x,line,virusFilePosition,virusLinePosition);
                if(self.MODE==1):
                    self.GarbageVirus(file,x,line,virusFilePosition,virusLinePosition);

            if(self.MODE==0):
                print("Successfully wrote B-Virus file: "+str(x));
            if(self.MODE==1):
                print("Successfully wrote G-Virus file: "+str(x));
            file.close(); #Close my file so I can do stuff with it.

    #Difficulty 1/5
    def BasicVirus(self,file,x,line,virusFilePosition,virusLinePosition):
        """
        A basic file that writes a bunch of text to a file. One of the lines in one of the files will be a message the students need to find.
        """
        #If the file I am writing to is the virus file and this line is where the virus needs to go....
        if(x==virusFilePosition and line==virusLinePosition):
            #Either chose words or garbage.
            file.write("I am the virus!\n");
            if(self.DEBUG):
                print("Virus file sucessfully written at file: "+str(x)+" at line: "+str(line))

        else: #Any other case for the file, get garbage of some sorts. Maybe random words or something.
            file.write("Not a virus\n");

    #Difficulty 3/5.... unless you use the str.in() function.
    def GarbageVirus(self,file,x,line,virusFilePosition,virusLinePosition):
        """
        Write the virus file but add garbage to it so that people can't just read for the answer. Though I suppose ctrl+f still works....
        """
        #Use a salt method?
        #If the file I am writing to is the virus file and this line is where the virus needs to go....
        if(x==virusFilePosition and line==virusLinePosition):
            ##Get random amount of padding on both sides of my message.
            GARBAGE_MAX=random.randint(1,100); #Random num 1-100
            GARBAGE_MAX2=random.randint(1,100); #Random num 1-100
            bits1=random.getrandbits(GARBAGE_MAX); #get some left padding random bits
            bits2=random.getrandbits(GARBAGE_MAX2); #get some right padding random bits

            file.write(str(bits1)); #Write left padding garbage
            file.write("I am the virus!"); #Write the actual virus message
            file.write(str(bits2)); #Write right padding garbage

            file.write("\n"); #Write a newline character so I can put more garbage on the next line.
            
            if(self.DEBUG):
                print("Virus file sucessfully written at file: "+str(x)+" at line: "+str(line))

        else: #Any other case for the file, get garbage of some sorts. Maybe random words or something.
            GARBAGE_MAX=random.randint(1,100); #Random num 1-100
            GARBAGE_MAX2=random.randint(1,100); #Random num 1-100
            bits1=random.getrandbits(GARBAGE_MAX); #get some left padding random bits
            bits2=random.getrandbits(GARBAGE_MAX2); #get some right padding random bits

            file.write(str(bits1)); #Write left padding garbage
            file.write(str(bits2)); #Write right padding garbage

            file.write("\n"); #Write a newline character so I can put more garbage on the next line.

