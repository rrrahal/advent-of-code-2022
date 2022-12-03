###                                              ###
###                                              ###
### TEMPLATE FOR READING THE INPUT/EXAMPLE TEXT  ###
###                                              ###
###                                              ###

example = None
real_input = None

with open("example.txt") as f:
  example = [line.strip() for line in f.readlines()]

with open("input.txt") as f:
  real_input = [line.strip() for line in f.readlines()]


#print("EXAMPLE >>", example)
#print("INPUT >>", real_input)


def get_most_calories(calories):
  max_calories = 0
  current_calories = 0
  for calorie in calories:
    if calorie == "":
      max_calories = max(max_calories, current_calories)
      current_calories = 0
    else:
      current_calories += int(calorie)
  return max_calories

#print("Example Solution: ", get_most_calories(example))
#print("Input solution: ", get_most_calories(real_input))

def get_top_three_elves(calories):
  total_calories = []
  current_calories = 0
  for calorie in calories:
    if calorie == "":
      total_calories.append(current_calories)
      current_calories = 0
    else:
      current_calories += int(calorie)
  total_calories.sort(reverse=True)
  return total_calories[0] + total_calories[1] + total_calories[2]

print("Example Solution 2: ", get_top_three_elves(example))
print("Example Solution 1: ", get_top_three_elves(real_input))


