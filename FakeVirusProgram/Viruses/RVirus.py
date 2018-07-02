from VirusProgram import Virus;
import path;
import random;

class RVirus(Virus):
    def __init__(self,Dir,MAX_NUMBER_OF_LINES,MAX_NUMBER_OF_FILES,MODE):
        #Constant variables.
        self.MAX_NUMBER_OF_LINES=100;
        self.MAX_NUMBER_OF_FILES=100;
        self.DEBUG=False; #Used to print debug messages to help figure out where to look.
        self.dir=Dir;
        self.MODE=MODE;
        wordy=open("words.txt","r");  
        self.words=wordy.readlines();
        
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
                    self.RSAVirus(file,x,line,virusFilePosition,virusLinePosition);
            
            if(self.MODE==0):
                print("Successfully wrote R-Virus file: "+str(x));
            file.close(); #Close my file so I can do stuff with it.
    def RSAVirus(self,file,x,line,virusFilePosition,virusLinePosition):
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!1Optimize this to not open a txt file for every line I'm writting......
        
        #We don't want too many words on a line. Makes it look terrible.
        GARBAGE_MAX=random.randint(1,25); #Random num 1-25
        GARBAGE_MAX2=random.randint(1,25); #Random num 1-25
        leftPadding="";
        rightPadding="";
        for i in range(0,GARBAGE_MAX):
            pos=random.randint(0,len(self.words)-1); #Get a random word for left padding.
            word=self.words[pos];
            leftPadding+=word+" ";
        for i in range(0,GARBAGE_MAX2):
            pos=random.randint(0,len(self.words)-1); #Get a random word for left padding.
            word=self.words[pos];
            rightPadding+=word+" ";

        value=0;

        if(x==virusFilePosition and line==virusLinePosition):
            msg=leftPadding+" I am the virus! "+rightPadding;
            for char in msg:
                value*=256;
                value+=ord(char);
            file.write(str(value)); #Write RSA Message.
        else:
            msg=leftPadding+rightPadding;
            for char in msg:
                value*=256;
                value+=ord(char);
            file.write(str(value)); #Write RSA Message.
