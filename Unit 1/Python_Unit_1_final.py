# Required_FINAL_Project_IntroPy #

# [ ] create, call and test the adding_report() function
# then PASTE THIS CODE into edX

def adding_report(report):
    total = 0
    items = ""
    while True:
        str_input = input("Enter an integer or 'quit': ")
        if str_input.isdigit() == False:
            if str_input.lower().startswith("q"):
                if report == "A":
                    print("\nItems:\n" + items)
                    print("Total:")
                    print(total)
                    break
                else:
                    print("\nTotal:")
                    print(total)
                    break
            else:
                print(str_input,"- is invalid input!")
        else:
            total = total + int(str_input)
            if report == "A":
                items = items + str_input + "\n"
# report = "T" 
report = "A"
adding_report(report)

# ------- End of module -------- #