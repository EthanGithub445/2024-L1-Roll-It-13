# finds the lowest, highest and average
# score from a list
def get_stats(stats_list):
    stats_list.sort()

    # find lowest, highest and average scores...
    user_low = stats_list[0]
    user_high = stats_list[-1]
    user_average = sum(stats_list) / len(stats_list)

    return [user_low, user_high, user_average]


# create lists to hold user and computer scores
user_points = [10, 0, 13, 7, 10, 11]
computer_points = [10, 11, 0, 0, 10, 11]

# loop six times for testing purposes, ask the user to enter the
# score for the user and the computer for each round
# for item in range(0, 6):
#     user_points = int(input("Enter the user score: "))
#     computer_points = int(input("Enter the computer score: "))
#
#     # add user score to the list of user scores
#     user_points.append(user_points)
#     computer_points.append(computer_points)

# calculate the lowest, highest and average
# scores and display them.

# # sort the lists.
# user_points.sort()
# computer_points.sort()
#
# # find lowest, highest and average scores...
# user_low = user_points[0]
# user_high = user_points[-1]
# user_average = sum(user_points) / len(user_points)

# calculate lowest highest and average scores
# and display them

user_stats = get_stats(user_points)
computer_points = get_stats(computer_points)

print("     Game Statistics     ")
print(f"User  - Lowest Score:   {user_stats[0]}\t "  
      f"Highest Score:  {user_stats[1]}\t "
      f"Average Score:  {user_stats[2]} ")

print(f"Computer   - Lowest Score: {computer_points[0]}\t "
      f"Highest Score: {computer_points[1]}\t "
      f"Average Score: {computer_points[2]}")
