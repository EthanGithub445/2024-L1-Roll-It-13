# create lists to hold user and computer scores
user_points = []
computer_points = []

# loop six times for testing purposes, ask the user to enter the
# score for the user and the computer for each round
for item in range(0, 6):
    user_points = int(input("Enter the user score: "))
    computer_points = int(input("Enter the computer score: "))

    # add user score to the list of user scores
    user_points.append(user_points)
    computer_points.append(computer_points)

# calculate the lowest, highest and average
# scores and display them.

# sort the lists.
user_points.sort()
computer_points.sort()

# find lowest, highest and average scores...
user_low = user_points[0]
user_high = user_points[-1]
user_average = sum(user_points) / len(user_points)

print("Low: ", user_low)
print("High: ", user_high)
print("Average ", user_average)