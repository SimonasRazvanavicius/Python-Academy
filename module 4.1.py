# -------- MODULE 4.1: -------- #

# -- MOD04_1-6.1_Intro_Python --#

# [Task 1]
# [ ] Say "Hello" with nested if
# [ ] Challenge: handle input other than y/n
hello_input = input("Hi, Please say 'Hello', okay? ('y' for Yes / 'n' for No) ")
print()
    
if hello_input.lower() == "y":
    hello_type = input("Are you willing to say Full 'Hello'? ('y' for Yes / 'n' for No) ")
    print()
    if hello_type.lower() == "y":
        print("HELLO!")
    elif hello_type.lower() == "n":
        print("HI!") 
    else:

        print("Sorry, your answer should have been y/n.. And not'"+ hello_type + "'")

elif hello_input.lower() == "n":
    print("Oh well.. *Friendly nod*")
        
else:
    print("Sorry, your answer should have been y/n.. And not'"+ hello_input + "'")
print()
print("Goodbye!")

# [Task 2]
# Nested if - testing for False
# Program: [ ] 3 Guesses
# --> use nested if statements complete the flowchart code
# --> create a birds string variable with the names of 1, 2, 3 or more birds to make it easier
# --> get bird_guess input and use bird_guess in bird_names to generate Boolean True/False
# --> if the the guess is wrong (False) create a sub test until the user has had 3 guesses
# [ ] Create the "Guess the bird" program 
birds = "pigeon,eagle,hawk,raven"
birds_array = birds.split(",")
bird_guess = input("Guess the name of the bird: ")

if bird_guess.lower() in birds_array:
    print("Yes, 1st try!")
else:
    bird_guess2 = input("Incorrect! Try again: ")
    if bird_guess2.lower() in birds_array:
        print("Yes, 2nd try!")
    else:
        bird_guess3 = input("Incorrect! Last try: ")
        if bird_guess3.lower() in birds_array:
            print("Yes, 3nd try!")
        else:
            print("Sorry, you are out of tries!")

# ----- End of sub-module ------#

# ------- End of module --------#