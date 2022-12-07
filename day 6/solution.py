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
example = example[0]
real_input = real_input[0]

def has_repeated_char(input, i):
  chars = input[i:i+4]
  my_set = set(chars)

  return len(chars) != len(my_set)

def has_repeated_char_2(input, i):
  chars = input[i:i+14]
  my_set = set(chars)

  return len(chars) != len(my_set)


def solution1(full_input):
  for i in range(len(full_input) - 5):
    if (not has_repeated_char(full_input, i)):
      return i + 4

def solution2(full_input):
  for i in range(len(full_input) - 15):
    if (not has_repeated_char_2(full_input, i)):
      return i + 14



#print("Example -> Solution 1: ", solution1(example))
#print("Solution 1: ", solution1(real_input))

## Solution 2

print("Example -> Solution 2: ", solution2(example))
print("Solution 2: ", solution2(real_input))
