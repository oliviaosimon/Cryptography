"""
cryptography.py
Author: Olivia Simon
Credit: 
    https://www.dotnetperls.com/round-python
    

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
#start code
import math
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
    
        #fit key to match message
    divvy = (len(message)/len(key))
    divvy = math.ceil(divvy)           #math.ceil rounds up
    
    
    message_list = list()
    key_list = list()
    for unit in message:     #message division to list
        unitList = list(unit)
        for i in unitList:
            part = associations.find(i)
        message_list.append(part)
    print(message_list)
    key = (key*divvy)
    for u in key:            #key division to list
        uList = list(u)
        for q in uList:
            partKey = associations.find(q)
        key_list.append(partKey)
    print(key_list)
    combo = list(zip(message_list, key_list))
    print(combo)
    

    
    
elif toDo == "d":
    #decrypt
    print("d")
    
elif toDo == "q":
    print("Goodbye!")
    
else:
    print("Did not understand command, try again.")



