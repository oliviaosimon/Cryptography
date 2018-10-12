"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
for x in associations:
    print(associations.find(x))
    
#inputs
toDo = input("Enter e to encrypt, d to decrypt, or q to quit: ")
if toDo == "e":
    #encrypt
    
elif toDo == "d":
    #decrypt
    
elif toDo == "q":
    print("Goodbye!")
    
else:
    print("Did not understand command, try again.")



