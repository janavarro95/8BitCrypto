```
Virus Heuristics Program. AKA The world's best anti virus.
V 1.0.0
Josh Navarro
7/1/18
```

# Welcome to the virus heuristics program!
This will mimic what anti virus programs tend to do by opening a virus program, scanning through it, and detecting any suspicious activity that shows up.

Your goal is to find the hidden message "I am the virus" hidden in one of the files in each directory.
This message will be hidden in a bunch of different ways and it is up to you to figure out what technique I used to hide this message! But don't worry
I left a message at the bottom to tell you what you should expect.


## Rules:
1. No opening up any files in the Viruses folder. These are to remain a secret for how the viruses are written.
2. No modifying any of the viruses in the Viruses folder.
3. However you go about solving the virus puzzles is up to you.
4. You will always be looking for the string "I am the virus!".
5. You may ask me for Python help on solving these problems.

If you delete all of the virus files you win! You made an anti virus program for my viruses!
## What to Expect:
- Plain Text
- ASCII
- HEX
- Shift Cyphers
- A super secret cypher that was based on a project I did. Note the R virus is SUPER HARD. Think of it as the hardest challenge.
	- Hint, I love the * + / % symbols.

....and maybe some more stuff when if/when I think of them.

Every directory has a different technique used on it to hide the message "I am the virus!" so every time you look through one of these directories you'll want to use a different technique.

To generate a new batch of viruses just run main.py that I give you and it will reset all of the viruses.

## How to go about this task.

1. Get a list of all the virus folders. You will want to make this flexible in the case I write more viruses. Hard coding the path might be a bad idea but you can do it if you need to.
2. Get a list of all of the files in each directory.
3. Read all of the lines of text in a file.
4. Decrypt each of the lines if necessary. Some files are not encrypted so you'll want to determine what directories have encrypted files and which don't.

### Hint: B is not encrypted.
5. Determine if that file has the string "I am the virus!"
6. If the file has the phrase "I am the virus!", delete the file and let the user know.
