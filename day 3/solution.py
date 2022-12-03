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


## How to get the value for each letter
## Lowercase, the value is ord(letter) - 96
## UpperCase the value is ord(letter) - 38

## Problem 1

def get_item_value(item):
  if (item.isupper()):
    return ord(item) - 38
  else:
    return ord(item) - 96

def get_repeating_item(rucksack):
  half = int(len(rucksack) / 2)
  first_half = rucksack[0:half]
  second_half = rucksack[half::]
  letters = {}
  for item in first_half:
    letters[item] = True

  for item in second_half:
    if item in letters:
      return item

def get_total_priorities(rucksacks):
  total_priority = 0
  for rucksack in rucksacks:
    item = get_repeating_item(rucksack)
    total_priority += get_item_value(item)

  return total_priority

#print("Example for Problem 1:", get_total_priorities(example))
#print("Solution for Problem 1:", get_total_priorities(real_input))

## Problem 2

def get_group_item(group1, group2, group3):
  total_items = group1 + group2 + group3
  for item in total_items:
    if (item in group1 and item in group2 and item in group3):
      return item

def get_group_priority(rucksacks):
  i = 0
  total_priority = 0
  while (i < len(rucksacks)):
    group1 = rucksacks[i]
    group2 = rucksacks[i+1]
    group3 = rucksacks[i+2]
    item = get_group_item(group1, group2, group3)
    i += 3
    total_priority += get_item_value(item)

  return total_priority

print("Example for Problem 2:", get_group_priority(example))
print("Solution for Problem 2:", get_group_priority(real_input))
