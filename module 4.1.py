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

# -- MOD04_1-6.2_Intro_Python --#

# [Task 1]
# Task 1
# Format using backslash (\) escape sequences
# [ ] print "\\\WARNING!///"
print("\"\\\\\\WARNING!///\"")

# [ ] print output that is exactly (with quotes): "What's that?" isn't a specific question.
print("\"What\'s that?\" isn\'t a specific question.")

# [ ] from 1 print statement output the text commented below using no spaces
# One     Two     Three
# Four    Five    Six
print("One\tTwo\tThree\nFour\tFive\tSix")

# [Task 2]

# Program: pre_word() Function
# Function has a single string parameter that it checks s is a single word starting with "pre"

# --> Check if word starts with "pre"
# --> Check if word .isalpha()
# --> if all checks pass: return True
# --> if any checks fail: return False
# --> Test
# --> --> get input using the directions: *enter a word that starts with "pre": *
# --> --> call pre_word() with the input string
# --> --> test if return value is False and print message explaining not a "pre" word
# --> --> else print message explaining is a valid "pre" word
# [ ] create and test pre_word()

def pre_word(string_input):
    if string_input.lower().startswith("pre"):
        check1 = True
    else:
        check = False
    if string_input.lower().isalpha():
        check2 = True
    else:
        check2 = False
    return check1 and check2

# [Task 5]
Fix the Errors
# [ ] review, run, fix
print("Hello\nWorld!")

# ----- End of sub-module ------#

# --Practice_MOD04_1-6_IntroPy--#

# [Task 1]
# [ ] print a string that outputs the following exactly: The new line character is "\n"
print("The new line character is \"\\n\"")

# [Task 2]
# [ ] print output that is exactly (with quotes): "That's how we escape!"
print("\"That\'s how we escape!\"")


# [Task 3]
# [ ] with only 1 print statement and using No Space Characters, output the text commented below  

# 1       one
# 22      two
# 333     three

print("1\tone\n22\ttwo\n333\tthree")

# [Task 4]


# ----- End of sub-module ------#

# ------- End of module --------#