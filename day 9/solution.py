import copy

import numpy as np

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

def get_new_tail_position(head_position, tail_position, direction, old_head_position):
  if (head_position == tail_position):
    return tail_position

  head_line = head_position[0]
  tail_line = tail_position[0]

  head_column = head_position[1]
  tail_column = tail_position[1]

  if (head_line == tail_line):
    if (abs(head_column - tail_column) == 1):
      return tail_position
    if (head_column > tail_column):
      tail_column += 1
      return (tail_line, tail_column)
    return (tail_line, tail_column-1)

  if (head_column == tail_column):
    if (abs(head_line - tail_line) == 1):
      return tail_position
    if (head_line > tail_line):
      tail_line += 1
      return (tail_line, tail_column)
    return (tail_line-1, tail_column)

  if (abs(head_position[0] - tail_position[0]) == 1 and abs(head_position[1] - tail_position[1]) == 1):
    return tail_position

  #if (direction == "U"):
  #  tail_position = (head_line+1, head_column)
  #if (direction == "D"):
  #  tail_position = (head_line-1, head_column)
  #if (direction == "R"):
  #  tail_position = (head_line, head_column-1)
  #if (direction == "L"):
  #  tail_position = (head_line, head_column+1)

  return old_head_position


def process_command(direction, head_position, tail_position):
  old_head_position = copy.deepcopy(head_position)
  head_line = head_position[0]
  head_column = head_position[1]

  if (direction == "U"):
    head_position = (head_line - 1, head_column)

  if (direction == "D"):
    head_position = (head_line + 1, head_column)

  if (direction == "R"):
    head_position = (head_line, head_column + 1)

  if (direction == "L"):
    head_position = (head_line, head_column - 1)

  tail_position = get_new_tail_position(head_position, tail_position, direction, old_head_position)

  return head_position, tail_position

## Problem 1

def solution1(input):
  steps = {
    "U": 0,
    "D": 0,
    "R": 0,
    "L": 0,
  }
  for move in input:
    strip = move.strip()
    direction = strip[0]
    value = int(strip[2])
    if (direction == "U"):
      steps["U"] += value
    elif(direction == "D"):
      steps["D"] += value
    elif(direction == "R"):
      steps["R"] += value
    elif(direction == "L"):
      steps["L"] += value

  maxH = (steps["R"] + steps["L"] + 2)
  maxV = (steps["U"] + steps["D"] + 2)
  initial_line = maxV // 2
  initial_column = maxH // 2

  matrix = [[0 for i in range(maxH + 1)] for j in range(maxV + 1)]

  head_position = (initial_line, initial_column)
  tail_position = (initial_line, initial_column)
  matrix[initial_line][initial_column] = 1

  for move in input:
    strip = move.strip()
    direction = strip[0]
    value = int(strip[2])
    for i in range(value):
      head_position, tail_position = process_command(direction, head_position, tail_position)
      matrix[tail_position[0]][tail_position[1]] = 1

  myArray = np.array(matrix)
  print(myArray)

  total_steps = 0

  for line in matrix:
    for element in line:
      if element == 1:
        total_steps += 1

  return total_steps


print("Example 1: Solution 1:", solution1(example))
print("Solution 1:", solution1(real_input))
