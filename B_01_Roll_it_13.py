# checks if user has entered yes or no


def yes_no(question):
    while True:
        response = input(question)

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes or no")

# displays instructions to user

# checks if user has entered an integer
# checks if integer is 13 or above


def int_check():

    while True:

        error = "Please enter an integer that is 13 or more."

        try:
            response = int(input("Enter an integer: "))

            # if integer is 13 or less print error message
            if response < 13:
                print(error)
            # if integer is 13 or above continue program
            else:
                return response

        except ValueError:
            print(error)


def instruction():
    print('''
    instructions:
    
    ''')

# Main routine


print()
print("🎲🎲Roll It 13🎲🎲")
print()

want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes" or want_instructions == "y":
    instruction()
if want_instructions == "no" or want_instructions == "n":
    print("program continues")

target_score = int_check()
print(target_score)
