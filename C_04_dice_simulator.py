import random

# generates an integer between 0 and 6
# to simulate the roll of a die

def roll_die():
    result = random.randint(1, 6)
    return  result

# main routine starts here
for item in range (0, 10):
    user_score = 0
    double_score = "no"

    # roll two dice
    roll_1 = roll_die()
    roll_2 = roll_die()

    # check if we have a double score opportunity
    if roll_1 == roll_2:
        double_score = "yes"

    # find the total points (so far)
    user_points = roll_1 + roll_2

    # show user the result
    print(f"Die 1: {roll_1} \t die2:{roll_2} \t Points: {user_points}")
    print(f"Double score opportunity: {double_score}")
