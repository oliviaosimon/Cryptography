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
  
x = 0
#inputs
while x == 0:
    toDo = input("Enter e to encrypt, d to decrypt, or q to quit: ")

    #Possibilities
    if toDo == "e":
        #encrypt
        x += 1
        message = input("Message: ")
        key = input("Key: ")
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
        key = (key*divvy)        #makes key longer than length of message so zip later contains all that is required
        for u in key:            #key division to list
            uList = list(u)
            for q in uList:
                partKey = associations.find(q)
            key_list.append(partKey)
        combo = list(zip(message_list, key_list))
    
        #equation
        combo_list = list()
        for a in combo:
             combo_list.append(a[0]+a[1])         #adds message to key
        
        #if bigger than associations list
        for x,val in enumerate(combo_list):
            if val > (len(associations)):
                combo_list[x] = abs((len(associations)-val))
    
        #output encrypted message
        final_list = list()
        for q in combo_list:
            final_list.append(associations[q])
        print(''.join(final_list))
        toDO = 'd'
        
    elif toDo == "d":
        #decrypt
        message = input("Message: ")
        key = input("Key: ")
        
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
        key = (key*divvy)        #makes key longer than length of message so zip later contains all that is required
        for u in key:            #key division to list
            uList = list(u)
            for q in uList:
                partKey = associations.find(q)
            key_list.append(partKey)
        combo = list(zip(message_list, key_list))
        #equation
        combo_list = list()
        for a in combo:
             combo_list.append(a[0]-a[1])      #subtracts key from message
             
        #if outputs less than associations list
        for x,val in enumerate(combo_list):
            if val > (len(associations)):
                combo_list[x] = (len(associations)+val)
        
        #output decrypted message
        final_list = list()
        for q in combo_list:
            final_list.append(associations[q])
        print(''.join(final_list))
        toDo = 'e'
        
    elif toDo == "q":
        print("Goodbye!")
        x+=1
        
    else:
        print("Did not understand command, try again.")
        x = 0
    
