import random


# generates an integer between 0 6
# to simulate roll dice

def roll_die():
    result = random.randint(1, 6)
    return  result

def two_rolls():
    double_score = "no"

    # roll two dice
    roll_1 = roll_die()
    roll_2 = roll_die()

    # check if we have a double score opportunity
    if roll_1 == roll_2:
        double_score = "yes"

    # find the total points so far
    user_points = roll_1 + roll_2

    # show user the result
    print(f"Die 1: {roll_1} \t Die 2: {roll_2}")

    return user_points, double_score

# main routine starts here
print("please press <enter> to begin this round: ")
input()

# get initial dice roll for user
user_first = two_rolls()
user_points = user_first[0]
double_points = user_first[1]


# tell the user if they are eligible for double points
if double_points == "no":
    double_feedback = ""
else:
    double_feedback = "if you win this round, you gain double points!"

# output initial move results
print(f"you rolled a total of {user_points}. {double_feedback}")
print()

# get initial dice rolls for computer
computer_first = two_rolls()
computer_points = computer_first[0]

print(f"The computer rolled a total of {computer_points}.")

# Loop (while both user / computer have <= 13 points)...
while computer_points <=13 and user_points <= 13:

    # ask user if they want to roll again, update
    # points / status
    print()
    roll_again = input("do you want to roll the dice (type no to pass): ")
    if roll_again == "yes":
        user_move = roll_die()
        user_points += user_move
        print(f"you rolled a {user_move}. you now have {user_points} points.")

    print("\nPress <enter> to continue...")
    input()

    # roll die for computer and update computer points
    computer_move = roll_die()
    computer_points += computer_move
    print(f"the computer rolled a {computer_move}. The computer"
          f" now has {computer_points}.")

    print()
    if user_points > computer_points:
        result = "You are ahead."
    else:
        result = "the computer is ahead oh nooo!1!!"

    print(f"***Round Update****: {result} ")
    print(f"{user_points} \t | \t computer score: {computer_points}")

# outside loop - double user points if they won and are eligible

# show rounds results
if user_points < computer_points:
    print("buh you lost and no points "
          "have been added to your total score. the computer's score has "
          f" increased by {computer_points} points")

# currently does not include double points!
else:
    print(f"buh you won the round and {user_points} points have "
          f"been added to your score")
