# checks if user has entered an integer
# checks if integer is 13 or above
while True:

    error = "Please enter an integer that is 13 or more."

    try:
        my_num = int(input("enter an integer: "))

        # if integer is 13 or less print error message
        if my_num < 13:
            print(error)
        # if integer is 13 or above continue program
        else:
            print("Your number is ", my_num)

    except ValueError:
        print(error)
