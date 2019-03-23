# --------- MODULE 1: --------- #


# -- MOD01_1-1.1_Intro_Python --#

# [Task 1]
# Program: "Hello World!" with comment
print("Hellow World!")

# [Task 2]
# Insert a new Code cell below with a comment describing the task
# edit cell: add print() with the message "after edit, save!"
# run the cell
print("after edit, save!")

# Insert another new cell
# Insert a new Code cell below
# edit cell: add print() with the message showing the keyboard Shortcut to save Ctrl + s
# run the cell
print("Ctrl + s")

# ----- End of sub-module ------#



# -- MOD01_1-1.2_Intro_Python --#

# [Task 1]
# print messages with "double quotes" and 'single' quotes¶
# [ ] enter a string in the print() function using single quotes
print('Yellow World 1!')
# [ ] enter a string in the print() function using double quotes
print("Yellow World 2!")

# [Task 2]
# [ ] print an Integer
print(5)
# [ ] print a strings made of Integer characters
print("55")

# [Task 3]
# Program: assigning values to a string
# - in the cell below
#   -> print the variable current_msg
#   -> assign a new string to current_msg
#   -> print the variable current_msg again
# - run the code cell above and then run the cell below
# { ] run cell above then run this cell after completing the code as directed
current_msg = "I am a string"
print(current_msg)
current_msg = "I am a new string"
print(current_msg)

# [Task 4]
# Assign a variable and print the value
# assign a string value to a variable student_name
# print the value of variable student_name

# [ ] assign a string value to a variable student_name
student_name = "Hermis"
# [ ] print the value of variable student_name
print(student_name)

# [ ] assign the student_name variable  a different string value (a different name)
student_name = "Hermis2"
# [ ] print the value of variable student_name
print(student_name)
# [ ] assign a 3rd different string value, to the variable name 
student_name = "Hermis3"
# [ ] print the value of variable name
print(student_name)

# change variable type with reassignment¶
# assigning a value to a variable called bucket
# print the value of bucket
# assign an Integer value (no quotes) to the variable bucket
# print the value of bucket

# [ ] assigning a value to a variable called bucket
bucket = "kibiras"
# [ ] print the value of bucket 
print(bucket)
# [ ] assign an Integer value (no quotes) to the variable bucket
bucket = 5555
# [ ] print the value of bucket 
print(bucket)

# [ ] print integer 123 number
print(123)
# [ ] print string "123" number
print("123")

# ----- End of sub-module ------#


# -- MOD01_1-1.3_Intro_Python --#

# [Task 1]
# Using type()
# Complete the "identify data types" tasks by assigning values to the variable  bucket and using type()

# [ ] show the type after assigning bucket = a whole number value such as 16 
bucket = 16
type(bucket)

# [ ] show  the type after assigning bucket = a word in "double quotes"
bucket = "string"
type(bucket)

# [ ] display the type of 'single quoting' (use single quotes) 
bucket = 'string'
type(bucket)

# [ ] display the type of "double quoting" (use double quotes)
type("string")

# [ ] display the type of "12" (use quotes)
type("12")

# [ ] display the type of 12 (no quotes)
type(12)

# [ ] display the type of -12 (no quotes)
type(-12)

# [ ] display the type of 12.0 (no quotes)
type(12.0)

# [ ] display the type of 1.55
type(1.55)

# [ ] find the type of the type(3) statement (no quotes) - just for fun
type(3)

# ----- End of sub-module ------#



# -- MOD01_1-1.4_Intro_Python --#


# [Task 1]
# String and Number Addition
# [ ] add 3 integer numbers
1 + 2 + 3

# [ ] add a float number and an integer number
3.14 + 5

# [ ] Add the string "This notebook belongs to " and a string with your first name
"This notebook belongs to " + "Simon"

# [ ] Create variables sm_number and big_number and assign numbers then add the numbers
sm_number = 5
big_number = 1000
sm_number + big_number

# [ ] assign a string value to the variable first_name and add to the string ", remember to save the notebook frequently"
first_name = "Simon"
first_name + ", remember to save the notebook frequently"

# [Task 2]
# create Integer addition and string addition output¶

# [ ] perform string addition in the variable named new_msg (add a string to "my favorite food is ")
new_msg = "My favorite food is" + " patatoes"
print(new_msg)

# [ ] perform Integer addition in the variable named new_msg (add 2 or more Integers)
new_sum = 0 + 2 + 3 + 5
print(new_sum)

# [ ] create and print a new string variable, new_msg_2, that concatenates new_msg + a literal string
new_msg_2 = new_msg + ", God Damn It!"
print(new_msg_2)

# [Task 3]

# Fix TypeError
# Review the code in the cells below and then run the code
# Fix any errors and run until the code no longer shows errors

# [ ] review and run the code - then fix any Errors
total_cost = 3 + 45
print(total_cost)

# [ ] review and run the code - then fix any Errors
school_num = "123"
print("the street number of Central School is " + school_num)

# [ ] Read and run the code - write a hypothesis for what you observe adding float + int
#  [ ] HYPOTHESIS: 
print(type(3.3)) # -> float
print(type(3))   # -> int
print(3.3 + 3)   # -> 6.3

# [Task 4]
# Fix Errors

# [ ] repair the syntax error 
print("my socks do not match")

# [ ] repair the NameError  
print("my socks match now") 

# [ ] repair the syntax error 
print("Save the notebook frequently")

# [ ] repair the NameError 
student_name = "Alton"
print(student_name)

# [ ] repair the TypeError
total = "3"
print(total + " students are signed up for tutoring")

# ----- End of sub-module ------#


# -- MOD01_1-1.5_Intro_Python --#
# [Extra Task]
# create the flying bird in character art in the Code cell below
print('_         _  ')
print(' \       /')
print('  \ . . /')
print('     V')

# create the capital letter "E" in character art in the Code cell below
# [ ] capital letter "E" character art
print('_____')
print('|')
print('|')
print('|____')
print('|')
print('|')
print('|____')

# ----- End of sub-module ------#

# ------- End of module --------#