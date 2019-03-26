# --------- MODULE 1: --------- #

# -- Mod1_2-1.1_Intro_Python -- #

# [Task 1]
# Work with individual string characters

# [ ] assign a string 5 or more letters long to the variable: street_name
# [ ] print the 1st, 3rd and 5th characters

test_string = "Bazaarvoice"
print(test_string[0]) # 1st
print(test_string[2]) # 3st
print(test_string[4]) # 5st

# [ ] Create an input variable: team_name - ask that second letter = "i", "o", or "u"
# [ ] Test if team_name 2nd character = "i", "o", or "u" and print a message
# note: use if, elif and else

team_name = input("Please enter a team name: ")
while len(team_name) <= 1:
    team_name = input("Please enter a team name, which has 2 or more characters: ")

if team_name[1].lower() == "i":
    print("2nd character in team name is 'i'!")
elif team_name[1].lower() == "o":
    print("2nd character in team name is 'o'!")
elif team_name[1].lower() == "u":
    print("2nd character in team name is 'u'!")
else:
    print("2n character in team name is not 'i', 'o' or 'u'!")

# [Task 2]

# [ ] assign a string 5 or more letters long to the variable: street_name
# [ ] print the last 3 characters of street_name
street_name = "antakalnio"
print(street_name[-1])
print(street_name[-2])
print(street_name[-3])

# [ ] create and assign string variable: first_name
# [ ] print the first and last letters of name
first_name = "Simonas"
print("First letter of the name \"" + first_name + "\" is " + first_name[0])
print("Last letter of the name \"" + first_name + "\" is " + first_name[-1])

# [Task 3]
# Fix the Errors

# [ ] Review, Run, Fix the error using string index
shoe = "tennis"
# print the last letter
print(shoe[-1])


# ----- End of sub-module ------#

# -- Mod1_2-1.2_Intro_Python -- #

# [Task 1]
# slice a string
# start & stop index

# [ ] slice long_word to print "act" and to print "tic"
long_word = "characteristics"
print(long_word[4:7])
print(long_word[11:14]) # alternatively print(long_word[-4:-1])

# [ ] slice long_word to print "sequence"
long_word = "Consequences"
print(long_word[3:-1])

# [Task 2]
# [ ] print the first half of the long_word
long_word = "Consequences"
print(long_word[:6])

# [Task 3]
# [ ] print the second half of the long_word
long_word = "Consequences"
print(long_word[6:])

# [Task 4]
# [ ] print the 1st and every 3rd letter of long_word
long_word = "Acknowledgement"
print(long_word[::3])

# [ ] print every other character of long_word starting at the 3rd character
long_word = "Acknowledgement"
print(long_word[2::2])

# [Task 5]
# [ ] reverse long_word
long_word = "stressed"
print(long_word[::-1])

# [ ] print the first 5 letters of long_word in reverse
long_word = "characteristics"
print(long_word[4::-1])

# [Task 6]
# [ ] print the first 4 letters of long_word
# [ ] print the first 4 letters of long_word in reverse
# [ ] print the last 4 letters of long_word in reverse
# [ ] print the letters spanning indexes 3 to 6 of long_word in Reverse
long_word = "timeline"
print(long_word[:4])
print(long_word[3::-1])
print(long_word[7:3:-1])
print(long_word[6:2:-1])


# ----- End of sub-module ------#

# -- Mod1_2-1.3_Intro_Python -- #

# [Task 1]
# iterate a String
# one character at a time

# [ ] Get user input for first_name
# [ ] iterate through letters in first_name 
#    - print each letter on a new line
first_name = input("Enter your name: ")
for x in first_name:
    print(x)

# [Task 2]
# Program: capitalize-io

# --> get user input for first_name
# --> create an empty string variable: new_name
# --> iterate through letters in first_name
# --> --> add each letter in new_name
# --> --> capitalize if letter is an "i" or "o" *(hint: if, elif, else)
# --> print new_name
# [ ] Create capitalize-io
fist_name = input("Please enter your name: ")
new_name = ""
for i in first_name:
    if i.lower() == "i" or i.lower() == "o":
        new_name += i.upper()
    else:
        new_name += i
        
print(new_name)

# [Task 3]
# String slicing and iteration

# [ ] create & print a variable, other_word, made of every other letter in long_word
long_word = "juxtaposition"
other_word = ""

for i in long_word[::2]:
    other_word += i
print(other_word)

# Mirror Color
# [ ] get user input, fav_color
# [ ] print fav_color backwards + fav_color
# example: "Red" prints "deRRed"
fav_color = input("Enter your favourite color: ")
fav_backwards = ""
for i in fav_color[::-1]:
    fav_backwards += i
    
print(fav_backwards + fav_color)

# ----- End of sub-module ------#

# -- Mod1_2-1.4_Intro_Python -- #

# [Task 1]
# len()

# [ ] use len() to find the midpoint of the string 
# [ ] print the halves on separate lines
random_tip = "wear a hat when it rains"
midpoint = int(len(random_tip)/2)
print(random_tip[:midpoint])
print(random_tip[midpoint:])

# [Task 2]
# .count()
# for letters: "e" and "a" in random_tip
# [ ] print letter counts 
# [ ] BONUS: print which letter is most frequent
random_tip = "wear a hat when it rains"
count_e = random_tip.count("e")
count_a = random_tip.count("a")

print("Letter 'e' is repeated", count_e, "times")
print("Letter 'a' is repeated", count_a, "times")

if count_e == count_a:
    print("Letter 'e' and letter 'a' are both repeated", count_e,"times")
elif count_e > count_a:
    print("Letter 'e' is repeated more frequent than letter 'a'")
else:
    print("Letter 'a' is repeated more frequent than letter 'e'")

# [Task 3]
#.find()

# [ ] print long_word from the location of the first and second "t"
long_word = "juxtaposition"
first_position = long_word.find("t")
second_position = long_word.find("t",first_position+1)
print(long_word[first_position:second_position])

# [Task 4]
# Program: print each word in a quote
# [ ] Print each word in the quote on a new line  
quote = "they stumble who run fast"
start = 0
space_index = quote.find(" ")
while space_index != -1:
    print(quote[:space_index])
    quote = quote[space_index + 1:]
    space_index = quote.find(" ")
    if space_index == -1:
        print(quote)

# ----- End of sub-module ------#

# -- Mod1_2-1_IntroPy_Practice--#

# [Task 1]
# Access String Characters
# working_string[index]

# [ ] access and print the second character from planet_name: "u"
planet_name = "Jupiter"
print(planet_name[1])
print(planet_name[-6])

# [ ] access and print the first character from planet_name: "J"
planet_name = "Jupiter"
print(planet_name[0])
print(planet_name[-7])

# [ ] access and print the first and last characters from planet_name
planet_name = "Jupiter"
print(planet_name[0])
print(planet_name[-1])

# [ ] using a negative index access and print the first character from planet_name: "J"
planet_name = "Jupiter"
print(planet_name[-7])

# [Task 2]
# slice
# working_string[start:stop]
# working_string[start:stop:step]

# [ ] print planet_name sliced into the first 3 characters and remaining characters
planet_name = "Neptune"
print(planet_name[:3])
print(planet_name[3:])

# [ ] print 1st char and then every 3rd char of wise_words
# use string slice with a step
wise_words = 'Play it who opens'
print(wise_words[::3])

# [ ] print planet_name in reverse
planet_name = "Neptune"
print(planet_name[::-1])

# [Task 3]
# iterate a String
# for letter in sentence:

# [ ] Get user input for 1 fav_food
# [ ] iterate through letters in fav_food 
#    - print each letter on a new line
fav_food = "pizza"
for i in fav_food:
    print(i)

# [ ] iterate work_tip string concatenate each letter to variable: new_string 
# [ ] concatenate the letter or a "-" instead of a space " "
# tip: concatenate string example: word = word + "a"
work_tip = "Good code is commented code"
new_string = ""
for i in work_tip:
    if i == " ":
        new_string += "-"
    else:
        new_string += i
print(new_string)

# [ ] Print the first 4 letters of name on new line
name = "Hiroto"
for i in name[:4]:
    print(i)

# [ ] Print every other letter from 2nd to last letter of name 
name = "Hiroto"
for i in name[1::2]:
    print(i)

# [Task 4]
# Program: Mystery Name
# --> get user input for first_name
# --> create an empty string variable: new_name
# --> iterate through letters in first_name Backwards
# --> --> add each letter to new_name as you iterate
# --> --> Replace the letter if "e", "t" or "a" with "?" (hint: if, elif, elif, else)
# --> print new_name
# example: "Alton" = "no?l?"

# [ ] Create Mystery Name
first_name = input("Please enter your name: ")
new_name = ""
for i in first_name[::-1]:
    if i.lower() == "e" or i.lower() == "t" or i.lower() == "a":
        new_name += "?"
    else:
        new_name += i
        
print(new_name)

# [Task 4]
# len(), .find(), .count()

# [ ] find and display the length of the string: topic
topic = "len() returns the length of a string"
print(len(topic))

# [ ] use len() to find and display the mid_pt (middle) index (+/- 1) of the string: topic
# note: index values are whole numbers
topic = "len() can take a sequence, like a string, as an argument"
topic_lengt = int(len(topic))
mid_part = int(topic_lengt / 2)
print(mid_part)

# [ ] print index where first instance of the word  "code" starts using .find()
work_tip = "Good code is commented code"
print(work_tip.find("code"))

# [ ] search for "code" in code_tip using .find() 
# [ ] search substring with substring index start= 13,end = last char
# [ ] save result in variable: code_index
# [ ] display index of where "code" is found, or print "not found" if code_index == -1
work_tip = "Good code is commented code"
code_index = work_tip.find("code")
substring = work_tip[13:]
# print(substring)
if code_index != -1:
    print("Word 'code' appears in", code_index,"position!")
else:
    print("Word 'code' was not found!")

# [Task 5]
# [ ] find and report (print) number of w's, o's + use of word "code"
work_tip = "Good code is commented code"
print("Report: letter 'w' is mentioned", work_tip.count("w") ,"times.")
print("Report: letter 'o' is mentioned", work_tip.count("o") ,"times.")
print("Report: word 'code' is mentioned", work_tip.count("code") ,"times.")

# [ ]  count times letter "i" appears in code_tip string
# [ ] find and display the index of all the letter i's in code_tip
# Remember: if .find("i") has No Match, -1 is returned
code_tip = "code a conditional decision like you would say it"
# code_tip = "asdasdasdasdasd asdasdasd asda sd asd as d"
print ("code_tip:" , code_tip)
counter_i = code_tip.count("i")
print("\nReport:")
print("Letter 'i' is mentioned", counter_i, "times!")
if code_tip.find('i') == -1:
    print("Letter 'i' was not found in code_tip!")
else:
    print("Letter 'i' positions:")
    position = 0
    for i in code_tip:
        if i.lower() == 'i':
            print(position)
        position += 1

# [Task 6]
# [] create words after "G"
# sample quote "Wheresoever you go, go with all your heart" ~ Confucius (551 BC - 479 BC)
quote = "Wheresoever you go, go with all your heart"
word = ""
counter = 0
for i in quote:
    counter += 1
    if i.isalpha():
        word += i
        if counter == len(quote):
            print(word.upper())
    else:
        if word[:-1].lower() > 'g' and word != "":
            print(word.upper())
            word = ""
        else:
            word = ""

# ----- End of sub-module ------#

# --Required_Code_MOD1_IntroPy--#

# Program: Words after "G"/"g"
# [] create words after "G" following the Assignment requirements use of functions, menhods and kwyowrds
# sample quote "Wheresoever you go, go with all your heart" ~ Confucius (551 BC - 479 BC)
# [] copy and paste in edX assignment page
quote = "Wheresoever you go, go with all your heart,,,,"
word = ""
counter = 0
for i in quote:
    counter += 1
    if i.isalpha():
        word += i
        if counter == len(quote):
            print(word.upper())
    else:
        if word[:-1].lower() > 'g' and word != "":
            print(word.upper())
            word = ""
        else:
            word = ""

# ----- End of sub-module ------#

# ------- End of module --------#