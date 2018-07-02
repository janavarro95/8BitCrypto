from VirusProgram import Virus
import path;
import random;
class DVirus(Virus):
    #Also known as the dictionary virus
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
                    self.DictionaryVirus(file,x,line,virusFilePosition,virusLinePosition);
                if(self.MODE==1):
                    self.DictionaryASCIIVirus(file,x,line,virusFilePosition,virusLinePosition);
                if(self.MODE==2):
                    self.DictionaryHEXVirus(file,x,line,virusFilePosition,virusLinePosition);
                if(self.MODE==3):
                    self.DHShiftVirus(file,x,line,virusFilePosition,virusLinePosition);
                if(self.MODE==4):
                    self.DAShiftVirus(file,x,line,virusFilePosition,virusLinePosition);
            
            if(self.MODE==0):
                print("Successfully wrote D-Virus file: "+str(x));
            if(self.MODE==1):
                print("Successfully wrote DA-Virus file: "+str(x));
            if(self.MODE==2):
                print("Successfully wrote DH-Virus file: "+str(x));
            if(self.MODE==3):
                print("Successfully wrote DHSH-Virus file: "+str(x));
            if(self.MODE==4):
                print("Successfully wrote DASH-Virus file: "+str(x));
            file.close(); #Close my file so I can do stuff with it.

    #Probably make a seperate class for this virus.
    def DictionaryVirus(self,file,x,line,virusFilePosition,virusLinePosition):
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

        if(x==virusFilePosition and line==virusLinePosition):
            file.write(leftPadding); #Write left padding garbage
            file.write("I am the virus!"); #Write the actual virus message
            file.write(rightPadding); #Write right padding garbage
        else:
            file.write(leftPadding); #Write left padding garbage
            file.write(rightPadding); #Write right padding garbage

    def DictionaryASCIIVirus(self,file,x,line,virusFilePosition,virusLinePosition):
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!1Optimize this to not open a txt file for every line I'm writting......
        
        #We don't want too many words on a line. Makes it look terrible.
        GARBAGE_MAX=random.randint(1,25); #Random num 1-25
        GARBAGE_MAX2=random.randint(1,25); #Random num 1-25
        leftPadding="";
        rightPadding="";

        leftASCII="";
        rightASCII="";
        for i in range(0,GARBAGE_MAX):
            pos=random.randint(0,len(self.words)-1); #Get a random word for left padding.
            word=self.words[pos];
            leftPadding+=word+" ";
        for i in range(0,GARBAGE_MAX2):
            pos=random.randint(0,len(self.words)-1); #Get a random word for left padding.
            word=self.words[pos];
            rightPadding+=word+" ";

        #Convert padding into ASCII
        for char in leftPadding:
            value=str(ord(char));
            leftASCII+=value+" ";
        for char in rightPadding:
            value=str(ord(char));
            rightASCII+=value+" ";
            
        if(x==virusFilePosition and line==virusLinePosition):
            file.write(leftASCII); #Write left padding garbage
            file.write("I am the virus!"); #Write the actual virus message
            file.write(rightASCII); #Write right padding garbage
        else:
            file.write(leftASCII); #Write left padding garbage
            file.write(rightASCII); #Write right padding garbage

    def DictionaryHEXVirus(self,file,x,line,virusFilePosition,virusLinePosition):
        #We don't want too many words on a line. Makes it look terrible.
        GARBAGE_MAX=random.randint(1,25); #Random num 1-25
        GARBAGE_MAX2=random.randint(1,25); #Random num 1-25
        leftPadding="";
        rightPadding="";

        leftASCII="";
        rightASCII="";
        for i in range(0,GARBAGE_MAX):
            pos=random.randint(0,len(self.words)-1); #Get a random word for left padding.
            word=self.words[pos];
            leftPadding+=word+" ";
        for i in range(0,GARBAGE_MAX2):
            pos=random.randint(0,len(self.words)-1); #Get a random word for left padding.
            word=self.words[pos];
            rightPadding+=word+" ";

        #Convert padding into ASCII
        for char in leftPadding:
            value=hex(ord(char));
            leftASCII+=value
        for char in rightPadding:
            value=hex(ord(char));
            rightASCII+=value;
        
        if(x==virusFilePosition and line==virusLinePosition):
            file.write(leftASCII); #Write left padding garbage
            msg="I am the virus!";
            hxMsg="";
            for char in msg:
                value=hex(ord(char));
                hxMsg+=value;
            file.write(hxMsg); #Write the actual virus message
            file.write(rightASCII); #Write right padding garbage
        else:
            file.write(leftASCII); #Write left padding garbage
            file.write(rightASCII); #Write right padding garbage

    #Difficulty 4.5/5
    def DHShiftVirus(self,file,x,line,virusFilePosition,virusLinePosition):
        GARBAGE_MAX=random.randint(1,25); #Random num 1-25
        GARBAGE_MAX2=random.randint(1,25); #Random num 1-25
        leftPadding="";
        rightPadding="";

        leftASCII="";
        rightASCII="";

        shift=random.randint(1,100);
        
        for i in range(0,GARBAGE_MAX):
            pos=random.randint(0,len(self.words)-1); #Get a random word for left padding.
            word=self.words[pos];
            leftPadding+=word+" ";
        for i in range(0,GARBAGE_MAX2):
            pos=random.randint(0,len(self.words)-1); #Get a random word for left padding.
            word=self.words[pos];
            rightPadding+=word+" ";

        #Convert padding into ASCII
        for char in leftPadding:
            value=hex((ord(char)+shift)%256);
            leftASCII+=value
        for char in rightPadding:
            value=hex((ord(char)+shift)%256);
            rightASCII+=value;
        
        if(x==virusFilePosition and line==virusLinePosition):
            file.write(leftASCII); #Write left padding garbage
            msg="I am the virus!";
            hxMsg="";
            for char in msg:
                value=hex((ord(char)+shift)%256);
                hxMsg+=value;
            file.write(hxMsg); #Write the actual virus message
            file.write(rightASCII); #Write right padding garbage
        else:
            file.write(leftASCII); #Write left padding garbage
            file.write(rightASCII); #Write right padding garbage
        
    def DAShiftVirus(self,file,x,line,virusFilePosition,virusLinePosition):
        GARBAGE_MAX=random.randint(1,25); #Random num 1-25
        GARBAGE_MAX2=random.randint(1,25); #Random num 1-25
        leftPadding="";
        rightPadding="";

        leftASCII="";
        rightASCII="";

        shift=random.randint(1,100);
        
        for i in range(0,GARBAGE_MAX):
            pos=random.randint(0,len(self.words)-1); #Get a random word for left padding.
            word=self.words[pos];
            leftPadding+=word+" ";
        for i in range(0,GARBAGE_MAX2):
            pos=random.randint(0,len(self.words)-1); #Get a random word for left padding.
            word=self.words[pos];
            rightPadding+=word+" ";

        #Convert padding into ASCII
        for char in leftPadding:
            value=str((ord(char)+shift)%256);
            leftASCII+=value+" ";
        for char in rightPadding:
            value=str((ord(char)+shift)%256);
            rightASCII+=value+" ";
        
        if(x==virusFilePosition and line==virusLinePosition):
            file.write(leftASCII); #Write left padding garbage
            msg="I am the virus!";
            hxMsg="";
            for char in msg:
                value=str((ord(char)+shift)%256);
                hxMsg+=value;
            file.write(hxMsg); #Write the actual virus message
            file.write(rightASCII); #Write right padding garbage
        else:
            file.write(leftASCII); #Write left padding garbage
            file.write(rightASCII); #Write right padding garbage
