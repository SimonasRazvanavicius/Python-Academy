# --------- MODULE 2: --------- #


# -- MOD02_1-3.1_Intro_Python --#

# [Task 1]
# Many Arguments can be passed to print
# update the print statement to use print() with 8 or more arguments
# increase the number of arguments used in print() to 8 or more 
student_age = 17
student_name = "Hiroto Yamaguchi"
print(student_name,'will','be','in','the,','class','for',student_age, 'year old students.')

# [Task 2]
# Define and call a simple function   yell_it()
# takes no arguments
# indented function code does the following
# define a variable for called phrase and intialize with a short phrase
# prints phrase as all upper-case letters followed by "!"
# call   yell_it   at the bottom of the cell after the function  def  (Tip: no indentation should be used)
# [ ] define (def) a simple function called yell_it() and call the function
def yell_it():
	phrase = "laba diena"
	print(phrase.upper() + "!")

yell_it();

# [Task 3]
# Define yell_this() and call with variable argument
# [ ] define yell_this() 
# [ ] get user input in variable words_to_yell
# [ ] call yell_this function with words_to_yell as argument
def yell_this(words_to_yell):
    print(words_to_yell)

words_to_yell = input()
yell_this(words_to_yell)


# ----- End of sub-module ------#




# -- MOD02_1-3.2_Intro_Python --#

# [Task 1]
# Doctor: a function that adds the "Doctor" title to a name
# create and call make_doctor() with full_name argument from user input - then print the return value

def make_doctor(name):
    return "Doctor " + name

full_name = input()
make_doctor(full_name)


# [Task 2]
# Define make_schedule() adding a 3rd period to
# --> Start with the above example code
# --> add a parameter period_3
# --> update function code to add period_3 to the schedule
# --> call student_schedule() with an additional argument such as 'science'
# --> print the schedule
# [ ] add a 3rd period parameter to make_schedule
# [ ] Optional - print a schedule for 6 classes (Tip: perhaps let the function make this easy)
def make_schedule(period1, period2, period3, period4, period5, period6):
    schedule = ("[1st] " + period1.title() + ", [2nd] " + period2.title() + ", [3rd] " + period3.title() + ", [4th] " + period4.title() + ", [5th] " + period5.title() + ", [6th] " + period6.title())
    return schedule

student_schedule = make_schedule("mathematics", "history", "algebra", "biology","english","chemistry")
print("SCHEDULE:", student_schedule)

# ----- End of sub-module ------#


# -- MOD02_1-3.3_Intro_Python --#

# [Task 1]
# Change the Sequence to fix the NameError
# [ ] fix the sequence of the code to remove the NameError

def hat_available(color):
    hat_colors = 'black, red, blue, green, white, grey, brown, pink'
    return(color.lower() in hat_colors)


have_hat = hat_available('green')  
  
print('hat available is', have_hat)

# [Task 2]
# Program: bird_available:
# The program should ask for user to "input a bird name to check for availability" and print a statement informing of availability
# create this program with a Boolean function bird_available()
# --> has parameter that takes the name of a type of bird
# --> for this exercise the variable bird_types = 'crow robin parrot eagle sandpiper hawk piegon'
# --> return True or False (we are making a Boolean function)
# --> call the function using the name of a bird type from user input
# --> print a sentence that indicates the availablity of the type of bird checked
# [ ] create function bird_available
# [ ] user input
# [ ] call bird_available
# [ ] print availbility status

def bird_available(bird_type):
    bird_types = 'crow robin parrot eagle sandpiper hawk piegon'
    return(bird_type.lower() in bird_types)

bird_type = input('Enter bird type to check: ')
print('bird available is',bird_available(bird_type))


# [Task 3]
# Fix The Error

# define function how_many
def how_many(): #keyword def was missing
    requested = input("enter how many you want: ")
    return requested

# get the number_needed
number_needed = how_many()
print(number_needed, "will be ordered")

# ----- End of sub-module ------#


# --Practice_MOD02_1-3_IntroPy--#

# Tasks
# [Task 1]
# [ ] define and call a function short_rhyme() that prints a 2 line rhyme
def short_rhyme():
    print("Roses are red")
    print("Violets are blue")

short_rhyme()


# [Task 2]
# [ ] define (def) a simple function: title_it() and call the function
# - has a string parameter: msg
# - prints msg in Title Case

def title_it(smg):
    return print(smg.title())

message = 'labas'
title_it(message)


# [Task 3]:
# [ ] get user input with prompt "what is the title?" 
# [ ] call title_it() using input for the string argument

def title_it(smg):
    return print(smg.title())

message = input("What is the title?")
title_it(message)


# [Task 4]
# [ ] define title_it_rtn() which returns a titled string instead of printing
# [ ] call title_it_rtn() using input for the string argumetnt and print the result

def title_it_rtn(msg):
    return msg.title()

message = input("Type the message, please:")
result = title_it_rtn(message)
print(result)

# [Task 5]
# Program: bookstore()
# create and test bookstore():
# --> bookstore() takes 2 string arguments: book & price
# --> bookstore returns a string in sentence form
# --> bookstore() should call title_it_rtn() with book parameter
# --> gather input for book_entry and price_entry to use in calling bookstore()
# --> print the return value of bookstore()

# [ ] create, call and test bookstore() function
def title_it_rtn(name):
    return name.title()

def bookstore(book, price):
    book_title = title_it_rtn(book)
    final_string = "Title: " + book_title + ", costs $" + price
    return final_string

book_entry = input("Enter book's title:")
price_entry = input("Enter book's price:")

print(bookstore(book_entry,price_entry))

# [Task 6]
# Fix the error
def make_greeting(name, greeting = "Hello"):
    return (greeting + " " + name + "!")

def get_name():
    name_entry = input("enter a name: ")
    return name_entry

def get_greeting():
    greeting_entry = input("enter a greeting: ")
    return greeting_entry

# get name and greeting, send to make_greeting 
print(make_greeting(get_name(), get_greeting()))

# ----- End of sub-module ------#

# --Required_Code_MOD2_IntroPy--#

# [Task 1]
# Program: fishstore()¶
# create and test fishstore():
# --> fishstore() takes 2 string arguments: fish & price
# --> fishstore returns a string in sentence form
# --> gather input for fish_entry and price_entry to use in calling fishstore()
# --> print the return value of fishstore()

# [ ] create, call and test fishstore() function 
def fishstore(fish, price):
    str = "Fish Type: " + fish.title() + " costs $"+ price
    return str

fish_entry = input("Enter the name of the fish: ")
price_entry = input("Enter the price of the fish: ")

fishstore(fish_entry, price_entry)

# ----- End of sub-module ------#

# ------- End of module --------#