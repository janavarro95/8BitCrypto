import os;
from os import listdir
from os.path import isfile, join

def combine(path, value):
    """
    Combine the path, C# style
    Params:
        path<string>: The base path to append to.
        value<string>: The path to append to the base path.
    """
    return path+"/"+value;

def createDirectory(path):
    """
    Checks if the directory exists. If it does not it creates it.
    Params:
        path<string>: The payth to the directory to create.
    """
    if not os.path.exists(path):
        os.makedirs(path);

def getWorkingDirectory():
    """
    Get the path to the current working directory.
    """
    return os.getcwd();

def getAllFiles(path):
    """
    Get a list of all of the files in the directory.
    Source:https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
    Params:
        path<string>: The directory path to search.
    """
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    return onlyfiles;

def getAllFilesWithFilter(path,Filter):
    """
    Get a list of all files in the directory that has a specific substring in the path, say like a file extension.
    Params:
        path<string>: The directory path to search.
        filter<string>: The substring to look for in the path. Typically something like .txt
    """
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    filterList=[];
    for file in onlyfiles:
        if(file.contains(Filter)):
            filterList.append(file);
    return filterList;

def getAllSubDirectories(path):
    """
    Get a list of all of my sub-directories in my current directory
    Params:
        path<string>: The directory path to search.
    """
    dirs=[];
    for x in os.listdir('.'): #Get all items in my current directory.
        if os.path.isdir(x): #If my item is a folder
            dirs.append(x); #Add it to my list of directories.
    return dirs;
