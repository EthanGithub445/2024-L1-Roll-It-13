print("🎲🎲Roll It 13🎲🎲")

want_instructions = input("Do you want to read the instructions? ")

if want_instructions == "yes" or want_instructions == "y":
    print("You chose yes")
elif want_instructions == "no" or want_instructions == "n":
    print("You chose no")
else:
    print("You did not choose a valid response")
