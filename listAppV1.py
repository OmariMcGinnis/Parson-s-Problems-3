"""
Program Goals:
1. Get input fromt he user (at multiple stages)
2. Convert some, but not all, inputs to ints from strings.
3. We need to provide the user with choices:
    a. Add more values to a list
    b. Return a value at a specific index position

"""
import random
myList = []

def mainProgram():
    while True:
        print("Hello, there! Let's work with lists!")
        print("Choose from the following options. Type a number!")
        choice = input("""1. Add to a list or
2. Return a value at an index
3. Random Search
4. Quit Program""")
        #add a way to catch bad user responses
        if choice == "1":
            addToList()
        elif choice == "2":
            indexValues()
        elif choice == "3":
            randomSearch
        else:
            break

def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!  ")
    myList.append(int(newItem))

def indexValues():
    print("Curious about an index position? ME TOO!")
    indexPos = input("What index position would you like to check out?  ")
    print(myList[int(indexPos)])

def randomSearch():
    print("RaNdOm SeArCh?!?")
    print(myList[random.randint(0, len(myList)-1]

    
#dunder main -> Double Underscore---dunder
if __name__ == "__main__":
    mainProgram()
