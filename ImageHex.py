import os;

basePath=os.getcwd();

fileName=input("Input an image file name.");

filePath=basePath+"/"+fileName;

with open(filePath, "rb") as imageFile:
    f = imageFile.read()
    b = bytearray(f)
    print(b);
