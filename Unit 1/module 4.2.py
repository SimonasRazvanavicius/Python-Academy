# -------- MODULE 4.2: -------- #

# -- MOD04_1-7.1_Intro_Python --#

# [Task 1]
# while True
# [ ] Program: Get a name forever ...or until done
# --> create variable, familar_name, and assign it an empty string ("")
# --> use while True:
# --> ask for user input for familar_name (common name friends/family use)
# --> keep asking until given a non-blank/non-space alphabetical name is received (Hint: Boolean string test)
# --> break loop and print a greeting using familar_name

# [ ] create Get Name program
family_name = ""
while True:
    family_name = input("Please type a family name: ")
    if family_name.lower().isalpha():
        print("Family name: " + family_name)
        break
    else:
        print("Family name is incorrect! Try again!")

# [Task 2]

# incrementing in a while() loop
# Program: Shirt Count
# --> enter a sizes (S, M, L)
# --> tally the count of each size
# --> input "exit" when finished
# --> report out the purchase of each shirt size

# [ ] Create the Shirt Count program, run tests
# initialize variables
t_shirt_count = 5
temp_count = 0
size_m = 0
size_s = 0
size_l = 0

while True:
    size_input = input('Enter what kind of T-shirt you would like to buy or "exit" (to finish): ')
    
    if size_input.lower() == "exit":
        print()
        break
    elif size_input.lower() == "m":
        size_m += 1
    elif size_input.lower() == "s":
        size_s += 1
    elif size_input.lower() == "l":
        size_l += 1
    else:
        print("Invalid size entry! TRY AGAIN!")
    temp_count = size_m + size_s + size_l
    if temp_count >= t_shirt_count:
        print("\nOut of T-shirts!")
        break
        
print("Total number of T-shirts:",temp_count,"\nSize M:",size_m,"\nSize S:",size_s,"\nSize L:",size_l)

# [Task 3]
# CHALLENGE: Shirt Register (optional)
# Update the Shirt Count program to calculate cost

# --> use shirt cost (S = 6, M = 7, L = 8)
# --> to calculate and report the subtotal cost for each size
# --> to calculate and report the total cost of all shirts

# [ ] Create the Shirt Register program, run tests
t_shirt_count = 5
temp_count = 0
temp_cost = 0
size_m = 0
size_s = 0
size_l = 0
cost_m = 7
cost_s = 6
cost_l = 8

while True:
    size_input = input('Enter what kind of T-shirt you would like to buy or "exit" (to finish): ')
    
    if size_input.lower() == "exit":
        print()
        break
    elif size_input.lower() == "m":
        size_m += 1
        temp_cost += cost_m
    elif size_input.lower() == "s":
        size_s += 1
        temp_cost += cost_s
    elif size_input.lower() == "l":
        size_l += 1
        temp_cost += cost_l
    else:
        print("Invalid size entry! TRY AGAIN!")
    temp_count = size_m + size_s + size_l
    if temp_count >= t_shirt_count:
        print("\nOut of T-shirts!")
        break
        
print("Total number of T-shirts:",temp_count,"\tTotal cost:",temp_cost)
print("Size S:",size_s,"\tSize S cost:",size_s*cost_s)
print("Size M:",size_m,"\tSize M cost:",size_m*cost_m)
print("Size L:",size_l,"\tSize L cost:",size_l*cost_l)

# ----- End of sub-module ------#

# -- MOD04_1-7.2_Intro_Python --#

# [Task 1]

# while with comparison operator
# Program: Animal Names
# --> Use while to get the user input, animal_name, of 4 animals
# --> --> use a counter, num_animals, in the while loop condition
# --> --> append the names to a string variable, all_animals
# --> --> User can exit early by typing "exit" (check if animal_name is "exit" and break)
# --> when the loop finishes, print the names of all_animals
# -bonus: print "no animals" if animal_name is empty after exiting the loop

# [ ] Create the Animal Names program, run tests
counter = 0
all_animals = ""
while counter < 4:
    animal_name = input("Please enter animals name (or type \"exit\", if you want stop): ")
    if animal_name.lower() == "exit":
        break
    elif animal_name.lower().isalpha():
        all_animals = all_animals + animal_name.lower() + ", "
        counter += 1
    else:
        print("Animal name is invalid, please try again!")

if counter > 0:
    print("Here is a list of all animals: " + all_animals[:-2])
else:
    print("There are no animals in the list!")

# [Task 2]
# Using while with a Boolean String
# Program: Long Number
# Create variables
# --> int_num and get user input string of only digits
# --> long_num and initialize it as an empty string
# Create a while loop that runs as long as the input is all digits
# Inside the while loop
# --> add int_num to the end of long_num
# --> get user input for int_num again (inside while loop this time)
# After the loop exits
# --> print the value of long_num

# [ ] Create the program, run tests
temp = 0
long_num = ""
int_num = ""
while int_num.isdigit() != True:
    int_num = input("Enter a digit (in numbers): ")
    if int_num.isdigit() == True:
        long_num = long_num + int_num
    while int_num.isdigit() == True:
        temp = 1
        int_num = input("Enter a digit (in numbers): ")
        if int_num.isdigit() == True:
            long_num = long_num + int_num
    if temp == 1:
        break

print(long_num)

# [Task 3]
# Fix the Errors
# This loop never runs
# This is a logic error - there is no ErrorMessage, but the code doesn't work

# [ ] review the code, run, fix the Logic error
count = 1

# loop 5 times
while count < 6:
    print(count, "x", count, "=", count*count)
    count +=1

# ----- End of sub-module ------#

# --Practice_MOD04_1-7_IntroPy--#

# [Task 1]
# [ ] use a "forever" while loop to get user input of integers to add to sum, 
# until a non-digit is entered, then break the loop and print sum
sum = 0
while True:
    digit_input = input("Enter a digit: ")
    if digit_input.isdigit() == True:
        sum = sum + int(digit_input)
    else:
        break
print("Total sum is:",sum)

# [Task 2]
# [ ] use a while True loop (forever loop) to give 4 chances for input of a correct color in a rainbow
# rainbow = "red orange yellow green blue indigo violet"
rainbow = ["red","orange","yellow","green","blue","indigo","violet"]
counter = 0
while True:
    guess = input("Name at least one color of the rainbow: ")
    counter += 1
    if guess in rainbow:
        print("Correct!",guess.title(),"is a color of the rainbow!")
        break
    else:
        print("Try again!")
    if counter >= 4:
        print("You are out of tries, GAME OVER!")
        break

# [Task 3]
# [ ] Get input for a book title, keep looping while input is Not in title format (title is every word capitalized)
title = ""
while title.istitle() != True:
    title = input("Please enter a title of the book: ")

print("The title of the book is: \"" + title + "\"")

# [Task 4]
# [ ] create a math quiz question and ask for the solution until the input is correct
answer = 826
guess = ""

while guess != "826":
    guess = input("Guess what is 800+26? ")

print("Correct! Congratz!")

# [Task 5]
# Fix the Error
# [ ] review the code, run, fix the error
tickets = input("enter tickets remaining (0 to quit): ")
while tickets.isdigit() != True:
    print("it's NOT a number! Please enter a number")
    tickets = input("enter tickets remaining (0 to quit): ")
tickets = int(tickets)

while tickets > 0:
        # if tickets are multiple of 3 then "winner"
    if int(tickets/3) == tickets/3:
        print("you win!")
        break
    else:
        print("sorry, not a winner.")
        break
    tickets = int(input("enter tickets remaining (0 to quit): "))

print("Game ended")

# [Task 6]
# create a function: quiz_item() that asks a question and tests if input is correct¶
# --> quiz_item()has 2 parameter strings: question and solution
# --> shows question, gets answer input
# --> returns True if answer == solution or continues to ask question until correct answer is provided
# --> use a while loop
# create 2 or more quiz questions that call quiz_item()
# Hint: provide multiple choice or T/F answers

# Create quiz_item() and 2 or more quiz questions that call quiz_item()
question1 = "What is the square root of 81?"
solution1 = "9"

question2 = "What is the square root of 100?"
solution2 = "10"

question3 = "What is the capital of Lithuania?"
solution3 = "Vilnius"

def quiz_item(question, solution):
    print("\n" + question)
    answer = ""
    while answer.lower() != solution.lower():
        answer = input("Please provide an answer: ")
        if answer.lower() == solution.lower():
            print("Correct! The answer is",solution)
        else:
            print("Incorrect! Please try again!")
        
quiz_item(question1,solution1)
quiz_item(question2,solution2)
quiz_item(question3,solution3)

# ----- End of sub-module ------#


# --Required_Code_MOD4_IntroPy--#

# Module 4 Required Coding Activity
# Program: str_analysis() Function



# ----- End of sub-module ------#

# ------- End of module --------#