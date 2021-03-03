# Parson-s-Problems-3
import random
myList = ['A1', 'B1', 'C1', 'D1', 'E1']

placeHolder = 0

message = ("Ready to continue?")

print("Grabbing a value")
print(random.choice(myList))

if placeHolder == 0:
    print("Random value printed!")

elif placeHolder == 1:
    print("Couldn't print a random value, oof!")

    while placeHolder < 0:
        print(message)
        if placeHolder == 0:
            break
        
        
