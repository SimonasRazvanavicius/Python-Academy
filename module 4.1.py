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
# Program: quote_me() Function
# quote_me takes a string argument and returns a string that will display surrounded with added double quotes if printed

# --> check if passed string starts with a double quote ("\""), then surround string with single quotations
# --> if the passed string starts with single quote, or if doesn't start with a quotation mark, then surround with double quotations
# Test the function code passing string input as the argument to quote_me()

# [ ] create and test quote_me()
test_string = input("Please enter a test string: ")

def quote_me(string_input):
    if string_input.lower().startswith("\""):
        print("\'" + test_string + "\'")
    else:
        print("\"" + test_string + "\"")

quote_me(test_string)

# [Task 5]

# Program: shirt order
# First get input for color and size
# 
# --> White has sizes L, M
# --> Blue has sizes M, S

# print available or unavailable, then
# print the order confirmation of color and size
# 
# * hint: set a variable "available = False" before nested if statements and
# change to True if color and size are avaliable*
# [ ] create shirt order using nested if 

t_color_availability = False

while not t_color_availability:
    t_color = input("Select color of a T-Shirt: ")
    if t_color.lower() == "white" or t_color.lower() == "blue" or t_color.lower() == "cancel":
        if t_color.lower() == "white" or t_color.lower() == "blue":
            t_color_availability = True
        else:
            print("Your order was cancelled!")
            break
    else:
        print()
        print("Please select another color. Right now we have only white and blue colors available! Type 'cancel' if you wish to stop your order")

t_size_availability = False
while not t_size_availability and t_color_availability:
    t_size = input("Select size of a T-Shirt: ")
    if (t_color.lower() == "white" and (t_size.lower() == "l" or t_size.lower() == "m")) or (t_color.lower() == "blue" and (t_size.lower() == "m" or t_size.lower() == "s")) or (t_size.lower() == "cancel"):
        if t_size.lower() != "cancel":
            t_size_availability = True
            print("Your order was complete!\nYou just bought " + t_color.title() + " t-shit (size: " + t_size.title() + ")")
        else:
            print("Your order was cancelled!")
            break
    else:
        if t_color.lower() == "white":
            print()
            print("Please select another size. Right now we have only L and M sizes for white t-shirt available! Type 'cancel' if you wish to stop your order")
        if t_color.lower() == "blue":
            print()
            print("Please select another size. Right now we have only M and S sizes for blue t-shirt available! Type 'cancel' if you wish to stop your order")

# [Task 6]
# Program: str_analysis() Function
# Create the str_analysis() function that takes a string argument. In the body of the function:

# --> Check if string is digits
# --> --> if digits: convert to int and check if greater than 99
# --> --> --> if greater than 99, print a message about a "big number"
# --> --> --> if not greater than 99, print message about "small number"
# --> --> if not digits: check if string isalpha
# --> --> --> if isalpha print message about being all alpha
# --> --> --> if not isalpha print a message about being neither all alpha nor all digit
# call the function with a string from user input

# [ ] create and test str_analysis()
string_input = input("Enter a string or a number: ")

def str_analysis(str_input):
    if str_input.isnumeric():
        int_number = int(str_input)
        if int_number > 99:
            print("Big number!")
        else:
            print("Small number!")
    elif str_input.isalpha():
        print("String is all alpha!")
    else:
        print("Sring (", str_input, ") is neither all alpha nor all digit!")
        
str_analysis(string_input)

# [Task 7]
# Program: ticket_check() - finds out if a seat is available
# Call ticket_check() function with 2 arguments: section and seats requested and return True or False

# --> section is a string and expects: general, floor
# --> seats is an integer and expects: 1 - 10
# Check for valid section and seats

# --> if section is general (or use startswith "g")
# --> --> if seats is 1-10 return True
# --> if section is floor (or use starts with "f")
# --> --> if seats is 1-4 return True
# otherwise return False

# [ ] create and call ticket_check()
# [ ] create and call ticket_check()
section = input("Enter the section: ")
seats = input("Enter the seat number: ")

def ticket_check(section, seats):
    seats_boolean = True
    section_boolean = True
    if section.lower() != "general" and section.lower() != "floor":
        print("Section is invalid!")
        section_boolean = False
    seats_array = ['1','2','3','4','5','6','7','8','9','10']
    seats_array2 = ['1','2','3','4']
    if not seats in seats_array:
        print("Seat is invalid!")
        seats_boolean = False
    if seats_boolean and section_boolean:
        if section.lower() == "floor" and not seats in seats_array2:
            print("Seat (" + seats + ") is not available in floor section")
        else:
            print("Seat (" + seats + ") is available in " + section + " section!")
    return seats_boolean and section_boolean

ticket_check(section, seats)

# ----- End of sub-module ------#

# ------- End of module --------#