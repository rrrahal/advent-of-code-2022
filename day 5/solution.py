###                                              ###
###                                              ###
### TEMPLATE FOR READING THE INPUT/EXAMPLE TEXT  ###
###                                              ###
###                                              ###

example = None
real_input = None

with open("example.txt") as f:
  example = [line for line in f.readlines()]

with open("input.txt") as f:
  real_input = [line for line in f.readlines()]


#print("EXAMPLE >>", example)
#print("INPUT >>", real_input)

def get_number_of_stacks(stacks):
  for stack in stacks:
    if stack[1] == '1':
      number_of_stacks = stack.strip()
      return int(number_of_stacks[-1])

def build_stacks(input, stacks, number_of_stacks):
  for line in input:
    start_index = 1
    for stack in range(1, number_of_stacks + 1):
      if (line[start_index] != " "):
        stacks[str(stack)].insert(0,line[start_index])
      start_index += 4
  return stacks

def apply_instructions(instructions, stacks):
  for ins in instructions:
    # filter digits here.
    digits = ins[5::]
    number_of_operations = ""
    i = 0
    while (digits[i].isdigit()):
      number_of_operations += digits[i]
      i += 1

    digits = digits[len(number_of_operations) + 6::]

    start_stack = ""
    i = 0
    while (digits[i].isdigit()):
      start_stack += digits[i]
      i += 1

    digits = digits[len(start_stack) + 4::]

    end_stack = ""
    i = 0
    while (len(digits) > i and digits[i].isdigit()):
      end_stack += digits[i]
      i += 1

    for i in range(int(number_of_operations)):
      el = stacks[start_stack].pop()
      stacks[end_stack].append(el)

  return stacks


def solution1(stacks_and_instructions):
  instructions = [ line.strip() for line in stacks_and_instructions if line.startswith("move") ]

  stacks_description = []
  for i in range(len(stacks_and_instructions)):
    if stacks_and_instructions[i].startswith(" 1"):
      stacks_description = stacks_and_instructions[:i]


  number_of_stacks = get_number_of_stacks(stacks_and_instructions)
  stacks = {}
  for i in range(1, number_of_stacks+1):
    stacks[str(i)] = []

  stacks = build_stacks(stacks_description, stacks, number_of_stacks)

  stacks = apply_instructions(instructions, stacks)

  final_word = ''

  for key in stacks:
    final_word += stacks[key][-1]

  return final_word


## Solution 2


def apply_instructions_2(instructions, stacks):
  for ins in instructions:
    # filter digits here.
    digits = ins[5::]
    number_of_operations = ""
    i = 0
    while (digits[i].isdigit()):
      number_of_operations += digits[i]
      i += 1

    digits = digits[len(number_of_operations) + 6::]

    start_stack = ""
    i = 0
    while (digits[i].isdigit()):
      start_stack += digits[i]
      i += 1

    digits = digits[len(start_stack) + 4::]

    end_stack = ""
    i = 0
    while (len(digits) > i and digits[i].isdigit()):
      end_stack += digits[i]
      i += 1

    last_valid_index = len(stacks[start_stack]) - int(number_of_operations)

    elements = stacks[start_stack][last_valid_index::]
    stacks[end_stack] += elements
    stacks[start_stack] = stacks[start_stack][:last_valid_index]

  return stacks

def solution2(stacks_and_instructions):
  instructions = [ line.strip() for line in stacks_and_instructions if line.startswith("move") ]

  stacks_description = []
  for i in range(len(stacks_and_instructions)):
    if stacks_and_instructions[i].startswith(" 1"):
      stacks_description = stacks_and_instructions[:i]


  number_of_stacks = get_number_of_stacks(stacks_and_instructions)
  stacks = {}
  for i in range(1, number_of_stacks+1):
    stacks[str(i)] = []

  stacks = build_stacks(stacks_description, stacks, number_of_stacks)

  stacks = apply_instructions_2(instructions, stacks)

  final_word = ''

  for key in stacks:
    final_word += stacks[key][-1]

  return final_word

#print("Example Solution 1: ", solution1(example))
#print("Solution 1: ", solution1(real_input))

print("Example Solution 2: ", solution2(example))
print("Solution 2: ", solution2(real_input))
