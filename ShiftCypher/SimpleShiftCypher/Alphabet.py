class Alphabet(object):
    def __init__(self,offset):
        self.offset=offset; #Can be neg or pos;
        self.letters={
            "a":0,
            "b":1,
            "c":2,
            "d":3,
            "e":4,
            "f":5,
            "g":6,
            "h":7,
            "i":8,
            "j":9,
            "k":10,
            "l":11,
            "m":12,
            "n":13,
            "o":14,
            "p":15,
            "q":16,
            "r":17,
            "s":18,
            "t":19,
            "u":20,
            "v":21,
            "w":22,
            "x":23,
            "y":24,
            "z":25,
        }

    #Returns the original letter associated with the value;
    def getLetter(self,number):
        for key in self.letters :
            if(self.letters[key]==number):
                return key;

    #Returns the offset that the letters dictionary is offsetted by.
    def getOffset(self,number):
        return self.offset;

    #Shift Cypher Encryption.
    """
    Params: self< Alphabet: reference to this object>, key< Char: Letter a-z to get the reference key to .>
    Returns: A key that is the value of the key passed in plus the offset value for this alphabet cypher.
    """
    def shiftEncryptLetter(self,key):
        key=key.lower(); #Lowercase the key for simplicity;
        value=self.letters[key]+self.offset;
        value=abs(value)%len(self.letters);
        newLetter=self.getLetter(value);
        return newLetter;

    #Ran on encrypted messages.
    def shiftDecryptLetter(self,key):
        key=key.lower();
        value=self.letters[key]-self.offset;
        value=value%len(self.letters);
        newLetter=self.getLetter(value);
        return newLetter;

    def encryptMessage(self,message):
        """Encrypts a secret message
        Params: (
            message<string>: The secret message to decrypt.
            )
        Returns: An encrypted message! <string>
        """
        value="";
        for letter in message:
            if(letter.lower() in self.letters):
               value+=self.shiftEncryptLetter(letter);
            else:
               value+=letter;
        return value;

    def decryptMessage(self,message):
        """Decrypts a secret message
        Params: (
            message<string>: The secret message to decrypt.
            )
        Returns: An decrypted message! <string>
        """
        value="";
        for letter in message:
            if(letter in self.letters):
               value+=self.shiftDecryptLetter(letter);
            else:
               value+=letter;
        return value;
    
