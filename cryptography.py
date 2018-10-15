"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
#for x in associations:
    #print(associations.find(x))
    
#inputs
toDo = input("Enter e to encrypt, d to decrypt, or q to quit: ")
message = input("Message: ")
key = input("Key: ")

#Possibilities
if toDo == "e":
    #encrypt
    while len(key) < len(message):
        key.append(key)
    for unit in message:
        unitList = list(unit)
        for i in unitList:
            part = associations.find(i)
        print(part)
    for unit in key:
        keyUnitList = list(unit)
        for i in keyUnitList:
            key = associations.find(unit)
        print(key)

        

    
    
elif toDo == "d":
    #decrypt
    print("d")
    
elif toDo == "q":
    print("Goodbye!")
    
else:
    print("Did not understand command, try again.")



