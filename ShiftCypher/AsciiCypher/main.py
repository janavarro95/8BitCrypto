msg=input("Enter a secret message");

new_msg="";

for char in msg:
    new_msg+=str(ord(char));
    new_msg+=" ";

print (new_msg);
