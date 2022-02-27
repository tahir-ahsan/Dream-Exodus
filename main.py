#!usr/bin/env python3

# imports
import re

# global variables
valid_name = "^[\w./-_ ]{1,7}$"

genderlist={
    1:["Male","he","his","him"],
    2:["Female","she","her","hers"],
    3:["Non-Binary","they","their","theirs"]
}

# to be made into modules
def playerInit():
    while True:
        name=input("Please input your name! Make sure it's 1-7 characters long, and only has letters, numbers, periods (.), underscores (_), and hyphens (-).\nEnter your name: ").upper()
        if not re.match(valid_name,name):
            print("Hey! Follow the instructions ;/\nInvalid name entered.")
        else:
            while True:
                gender=input("Please input your gender! 1 = Male; 2 = Female; 3 = Non-Binary.\nEnter your gender code: ")
                try:
                    gender=int(gender)
                    if gender in (1,2,3):
                        print(f"Great! Enjoy your adventure, {name}!")
                        break
                    else:
                        print("Hey! Follow the instructions ;/\nInvalid code entered.")
                except ValueError:
                    print("Hey! Follow the instructions ;/\nInvalid input entered (not a number).")
            break
    return name,gender,genderlist[gender][0]

# oop
class Player:
    def __init__(self):
        self.name,self.genderKey,self.gender=playerInit()

# main loop
def main():
    player=Player()

# execution code
if __name__== "__main__":
    main()