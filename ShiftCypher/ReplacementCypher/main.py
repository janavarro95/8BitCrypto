#Replacement Cypher
import getpass;

alphabet="abcdefghijklmnopqrstuvwxyz";
newAlphabet="zyxwvutsrqponmlkjihgfedcba";

message=getpass.win_getpass("Enter a secret message: ");

newMessage="";
for letter in message:
    index=alphabet.find(letter.lower());
    if(index==-1):
        newMessage+=letter;
    else:
        newLetter=newAlphabet[index];
        newMessage+=newLetter;

print("Your new message is: "+newMessage);
