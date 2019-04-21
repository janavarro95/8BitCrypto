from Alphabet import Alphabet;
#Make a mode for encrypting or decrypting a message.
val=input("Please chose to encrypt(e), decrypt(d), or brute force(b) a message");
base=Alphabet(0);
while(val!="d" and val!="e" and val!="b"):
    print("Invalid input. Please try again.");
    val=input("Please chose to encrypt(e), decrypt(d), or brute force(b) a message");
val=val.lower(); #Unify input.
if(val=="e"):
    message=input("Enter a secret message!: ");
    offset=input("Enter a number 0-26 to offset these values by: ");
    while(not offset.isdigit()):
        print("Invalid input. Please try again.");
        offset=input("Enter a number 0-26 to offset these values by: ");
    offset=int(offset)%len(base.letters);
    alph=Alphabet(offset);
    print("Your secret message is: "+alph.encryptMessage(message));
if(val=="d"):
    message=input("Enter a secret message!: ");
    offset=input("Enter a number 0-26 to offset these values by: Hint if you know the offset type it in. ");
    offset=int(offset)%len(base.letters);
    alph=Alphabet(offset);
    print("Your secret message is: "+alph.decryptMessage(message));
if(val=="b"):
    message=input("Enter a secret message!: ");
    for i in range(0,len(base.letters)):
        offset=i;
        offset=offset%len(base.letters);
        alph=Alphabet(offset);
        print("Your secret message is: "+alph.decryptMessage(message));
