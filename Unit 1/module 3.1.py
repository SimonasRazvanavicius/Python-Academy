# -------- MODULE 3.1: -------- #

# -- MOD03_1-4.1_Intro_Python --#

# [Task 1]
# Conditionals
sunny_today = True
# [ ] test if it is sunny_today and give proper responses using if and else
if sunny_today:
    print("Today is a sunny day")
else:
    print("Today is not a sunny day")

sunny_today = False
# [ ] use code you created above and test sunny_today = False
if sunny_today:
    print("Today is a sunny day")
else:
    print("Today is not a sunny day")

# [Task 2]
# Evaluating Boolean Conditionals
# create evaluations for .islower()
# --> print output describing if each of the 2 strings is all lower or not

test_string_1 = "welcome"
test_string_2 = "I have $3"
# [ ] use if, else to test for islower() for the 2 strings

if test_string_1.islower():
    print("First string is lower-case")
else:
    print("First string is not lower-case")

if test_string_2.islower():
    print("Second string is lower-case")
else:
    print("Second string is not lower-case")

# create a functions using startswith('w')
# --> w_start_test() tests if starts with "w"
# --> function should have a parameter for test_string and print the test result

test_string_1 = "welcome"
test_string_2 = "I have $3"
test_string_3 = "With a function it's efficient to repeat code"
# [ ] create a function w_start_test() use if & else to test with startswith('w')
def w_start_test(str):
    result = ""
    if str.startswith("w"):
        result = "string starts with letter \"w\""
    else:
        result = "string does not starts with letter \"w\""
    print("\""+str+"\" "+result)
# other option would be to write "return result" return 

# [ ] Test the 3 string variables provided by calling w_start_test()
w_start_test(test_string_1)
w_start_test(test_string_2)
w_start_test(test_string_3)

# ----- End of sub-module ------#


# -- MOD03_1-4.2_Intro_Python --#

# [Task 1]
# comparison operators
x = 9 + 4
# [ ] create a test to print() True or False for x is equal to 13
print("Is x equal to 13?", x == 13)

# [ ] create a test to print True or False for 3 + 3 is greater than 2 + 4
print("Is 3 + 3 greater than 2 + 4?", 3+3>2+4)

# [Task 2]
# Evaluating a comparison operator in if
# [ ] create an if/else statement that tests if y is greater than or equal x + x 
# [ ] print output: "y greater than or equal x + x is" True/False ...or a similar output
x = 3
y = x + 8
if y >= x + x:
    print("y great than or equal than x + x is True")
else:
    print("y great than or equal than x + x is False")

# ----- End of sub-module ------#


# -- MOD03_1-4.3_Intro_Python --#

# [Task 1]
# String Comparisons
msg = "Hello"
# [ ] print the True/False results of testing if msg string equals "Hello" string
print("Lets check if 'Hello' string is equal to variable msg: ","Hello" == msg)

greeting = "Hello"
# [ ] get input for variable named msg, and ask user to 'Say "Hello"'
# [ ] print the results of testing if msg string equals greeting string

msg = input("Please say Hello, just write 'Hello':")
print("Let's check if your message is equal to greeting string/variable:", msg == greeting)

# [Task 2]
# Conditionals: comparison operators with if

# [ ] get input for a variable, answer, and ask user 'What is 8 + 13? : '
# [ ] print messages for correct answer "21" or incorrect answer using if/else
# note: input returns a "string"

answer = input("What is 8 + 13?: ")
if answer == "21":
    print("Correct! It's 21")
else:
    print("Incorrect! Correct answer is 21!")

# [Task 3]
# Define and use tf_quiz() function
# ->tf_quiz() has 2 parameters which are both string arguments
# -> --> question: a string containg a T/F question like "Should save your notebook after edit?(T/F): "
# -> --> correct_ans: a string indicating the correct answer, either "T" or "F"
# ->tf_quiz() returns a string: "correct" or "incorrect"
# ->Test tf_quiz(): create a T/F question (or several!) to call tf_quiz()

# [ ] Create the program, run tests
def tf_quiz(question,correct_ans):
    result = ""
    print(question+" "+correct_ans)
    if correct_ans == "T":
        result = "Correct!"
    elif correct_ans == "F":
        result == "Incorrect!"
    else:
        resutl = "Underdefined!"
    return result

print("Answer is: "+tf_quiz("Should save your notebook after edit?:","T"))

# ----- End of sub-module ------#

# --Practice_MOD03_1-4_IntroPy--#

# [Task 1]
# [ ] input avariable: age as digit and cast to int
# if age greater than or equal to 12 then print message on age in 10 years 
# or else print message "It is good to be" age

age = input("Please enter your age: ")
if not age.isnumeric():
    print("Incorrect age")
else:
    age_int = int(age)

if age_int >= 12:
    print("Your age after 10 years will be:",age_int+10)
else:
    print("It is good to be",age_int,"years old!")

# [Task 2]
# [ ] input a number 
# if number IS a digit string then cast to int
# print number "greater than 100 is" True/False
# if number is NOT a digit string then message the user that "only int is accepted"

number = input("Please enter a number: ")
if not number.isnumeric():
    print("Incorrect number - only int is accepted")
else:
    number_int = int(number)

print("Your number (",number_int,") is greater than 100 ->", number_int>100)

# [Task 3]
# Guessing a letter A-Z
# check_guess() takes 2 string arguments: letter and guess (both expect single alphabetical character)

# [ ] create check_guess()
# call with test
letter = "J"
guess = "F"

def check_guess (guess, letter):
    if not guess.isalpha():
        print("Invalid")
        return False
    if letter == guess.upper():
        return True
    elif letter < guess.upper():
        print ("Your guess is High")
        return False
    else:
        print ("Your guess is Low")
        return False

res = check_guess (guess, letter)
if res:
    print("Your answer is correct!",res)
else:
    print("The right answer was:",letter)
    print(res)

# [Task 4]
# [ ] call check_guess with user input
letter = "J"
guess = input("Enter your guess (1 letter): ")

def check_guess (guess, letter):
    if not guess.isalpha():
        print("Invalid")
        return False
    if letter == guess.upper():
        return True
    elif letter < guess.upper():
        print ("Your guess is High")
        return False
    else:
        print ("Your guess is Low")
        return False

res = check_guess (guess, letter)
if res:
    print("Your answer is correct!",res)
else:
    print("The right answer was:",letter)
    print(res)

# [Task 5]
# Letter Guess
# create letter_guess() function that gives user 3 guesses

# --> takes a letter character argument for the answer letter
# --> gets user input for letter guess
# --> calls check_guess() with answer and guess
# --> End letter_guess if
# --> --> check_guess() equals True, return True
# --> --> or after 3 failed attempts, return False
# --> [ ] create letter_guess() function, call the function to test
letter = "J"
tries = 3

def check_guess (guess, letter):
    if not guess.isalpha():
        print("Invalid")
        return False
    if letter == guess.upper():
        return True
    elif letter < guess.upper():
        print ("Your guess is High")
        return False
    else:
        print ("Your guess is Low")
        return False

def letter_guess():
    for i in range(tries):
        guess = input ("Enter your guess ")
        res = check_guess (guess, letter)
        if res:
            print ("Correct!")
            return True
    return False

result = letter_guess()
if result:
    print ("Congratulations")
else:
    print ("The answer was ",letter)
print ("GAME OVER!")

# [Task 6]
# Pet Conversation
# ask the user for a sentence about a pet and then reply

# --> get user input in variable: about_pet
# --> using a series of if statements respond with appropriate conversation
# --> --> check if "dog" is in the string about_pet (sample reply "Ah, a dog")
# --> --> check if "cat" is in the string about_pet
# --> --> check if 1 or more animal is in string about_pet
# --> no need for else's
# --> finish with thanking for the story
# [ ] complete pet conversation

about_pet = input("What kind of pet do you have? Could you tell something about your pet?")

def check_animal(pet_string):
    animal_array = ["dog","cat","fish","bird"]
    i = 0
    for i in range(len(animal_array)):
        if animal_array[i] in pet_string.lower():
            print("Oh, you have a "+ animal_array[i] + "! How nice!")
    print("Thank you for the story!")
check_animal(about_pet)

# ----- End of sub-module ------#

# ------- End of module --------#