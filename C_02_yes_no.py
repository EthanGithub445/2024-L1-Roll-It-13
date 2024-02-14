# checks if user has entered yes or no
def yes_no(question):
    response = input(question)

    if response == "yes" or response == "y":
        return "yes"
    elif response == "no" or response == "n":
        return "no"
    else:
        print("You did not choose a valid response")
# Main Routine
want_instructions = yes_no("Do you want to read the instructions? ")
print(f"you chose {want_instructions}")
