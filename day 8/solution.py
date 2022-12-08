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


## Problem 1

def check_top(input, line, column):
  current_value = input[line][column]

  for i in range(line):
    if (input[i][column] >= current_value):
      return False

  return True

def check_bottom(input, line, column):
  number_of_lines = len(input)

  current_value = input[line][column]

  for i in range(line + 1, number_of_lines):
    if (input[i][column] >= current_value):
      return False

  return True

def check_right(input, line, column):
  number_of_columns = len(input[0])

  current_value = input[line][column]

  for i in range(column + 1, number_of_columns):
    if (input[line][i] >= current_value):
      return False

  return True

def check_left(input, line, column):
  current_value = input[line][column]

  for i in range(column):
    if (input[line][i] >= current_value):
      return False

  return True


def is_visible_tree(input, line, column):
  number_of_lines = len(input)
  number_of_columns = len(input[0])
  if (line == 0 or column == 0 or line == (number_of_lines - 1) or column == (number_of_columns - 1)):
    return True

  if (check_top(input, line, column) or check_bottom(input, line, column) or check_left(input, line, column) or check_right(input, line, column)):
    return True

  return False


def solution1(input):
  number_of_lines = len(input)
  number_of_columns = len(input[0])

  number_of_visible_tress = 0

  for line in range(number_of_lines):
    for column in range(number_of_columns):
      if (is_visible_tree(input, line, column)):
        number_of_visible_tress += 1

  return number_of_visible_tress


#print("Example -> Solution 1: ", solution1(example))
#print("Solution 1: ", solution1(real_input))

## Problem 2

def get_scenic_top(input, line, column):
  current_value = input[line][column]
  scenic_value = 0
  for i in range(line-1, -1, -1):
    if (current_value > input[i][column]):
      scenic_value += 1
    else:
      return scenic_value + 1

  return scenic_value

def get_scenic_bottom(input, line, column):
  number_of_lines = len(input)

  current_value = input[line][column]
  scenic_value = 0
  for i in range(line+1, number_of_lines):
    if (current_value > input[i][column]):
      scenic_value += 1
    else:
      return scenic_value + 1

  return scenic_value

def get_scenic_left(input, line, column):
  current_value = input[line][column]
  scenic_value = 0

  for i in range(column-1, -1, -1):
    if (current_value > input[line][i]):
      scenic_value += 1
    else:
      return scenic_value + 1

  return scenic_value

def get_scenic_right(input, line, column):
  number_of_columns = len(input[0])

  current_value = input[line][column]
  scenic_value = 0
  for i in range(column+1, number_of_columns):
    if (current_value > input[line][i]):
      scenic_value += 1
    else:
      return scenic_value + 1

  return scenic_value

def get_scenic_value(input, line, column):
  number_of_lines = len(input)
  number_of_columns = len(input[0])
  if (line == 0 or column == 0 or line == (number_of_lines - 1) or column == (number_of_columns - 1)):
    return 0

  top = get_scenic_top(input, line, column)
  bottom = get_scenic_bottom(input, line, column)
  left = get_scenic_left(input, line, column)
  right = get_scenic_right(input, line, column)

  return top * bottom * left * right

def solution2(input):
  number_of_lines = len(input)
  number_of_columns = len(input[0])

  max_scenic_value = 0

  for line in range(number_of_lines):
    for column in range(number_of_columns):
      scenic_value = get_scenic_value(input, line, column)
      max_scenic_value = max(max_scenic_value, scenic_value)

  return max_scenic_value

print("Example -> Solution 2: ", solution2(example))
print("Solution 2: ", solution2(real_input))


