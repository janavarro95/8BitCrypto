hexx="0123456789ABCDEF"

#Get msg
msg= input("Enter a message");

hexxMsg="";
#For each char in msg
for char in msg:
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
    hexxMsg+=" ";

#Print hex message.
print(hexxMsg);
