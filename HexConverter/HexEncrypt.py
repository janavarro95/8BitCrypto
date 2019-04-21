import os;
from os import listdir
from os.path import isfile, join

basePath=os.getcwd();
mypath=os.getcwd();
mypath+="/FilesToEncrypt";
encryptPath="/Secrets";
print(mypath)

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print(onlyfiles);


hexx="0123456789ABCDEF"
for file in onlyfiles:
    print ("Encrypting file :"+file);
    with open(mypath+"/"+file) as f:
        msg = f.readlines()
        hexxMsg="";
        for line in msg:
            print(line);
            #For each char in msg
            for char in line:
                #char to int with ascii
                val=ord(char);
                #convert
                first=int(val/16);
                second=int(val%16);

                #Get hex reference
                first_char=hexx[first];
                second_char=hexx[second];
                combine=first_char+second_char;

                hexxMsg+=combine;
            #Print hex message.
            print(hexxMsg);
            name=basePath+encryptPath+"/"+file+".secret";
            enc=open(name,"w");
            enc.write(hexxMsg);
            print("Wrote: "+name);
            enc.close();
            
