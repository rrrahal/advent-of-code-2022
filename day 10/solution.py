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



def solution1(input):
  register = 1
  cycles = [register]
  for ins in input:
    ins = ins.split()
    instruction = ins[0]
    value = None
    if (instruction == "addx"):
      value = int(ins[1])
      cycles.append(register)
      cycles.append(register + value)
      register = register + value
    else:
      cycles.append(register)
  i = 19
  total_sum = 0
  while (i < len(cycles)):
    total_sum += (i + 1) * cycles[i]
    i += 40
  return total_sum

#print("Example 1, solution 1:", solution1(example))
#print("Solution 1: ", solution1(real_input))

## Problem 2

def get_draw(cycle, register):
  if (abs(cycle - register) <= 3):
    return "#"
  else:
    return "."


def solution2(input):
  register = 1
  cycles = [register]
  for ins in input:
    ins = ins.split()
    instruction = ins[0]
    value = None
    if (instruction == "addx"):
      value = int(ins[1])
      cycles.append(register)
      cycles.append(register + value)
      register = register + value
    else:
      cycles.append(register)

  final_draw = ""
  position = 0
  for i in range(len(cycles)):
    if (position % 40 == 0):
      position = 0
      final_draw += "\n"

    if(abs(position - cycles[i]) <= 1):
      final_draw += "#"
      position += 1
    else:
      final_draw += '.'
      position += 1
  return final_draw


print("Solution 2, example: \n",  solution2(example))
print("Solution 2: ", solution2(real_input))
