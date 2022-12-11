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

def execute(op, left, right):
  if (op == "+"):
    return left + right
  if (op == "-"):
    return left + right
  if (op == "*"):
    return left * right
  raise ValueError("Operation not supported")

def get_operation(instruction):
  operation = instruction.split("=")[1]
  operation = operation.split()

  def execute_operation(current_value):
    left = current_value if operation[0] == "old" else int(operation[0])
    right = current_value if operation[2] == "old" else int(operation[2])

    return execute(operation[1], left, right)

  return execute_operation

def get_test(instruction):
  if "divisible" not in instruction:
    raise ValueError("Test not supported")

  value = int(instruction[18:])

  def test_fn(current_item_value):
    return current_item_value % value == 0

  return test_fn

def add_monkey(monkeys, instructions):
  monkey_number = instructions[0].split()[1][:-1]

  items = [ int(num) for num in instructions[1][15::].split(",") ]

  operation = get_operation(instructions[2])

  test = get_test(instructions[3])
  div_by = int(instructions[3][18:])

  tru = int(instructions[4].split()[-1])
  fal = int(instructions[5].split()[-1])

  monkeys[str(monkey_number)] = {
    "items": items,
    "operation": operation,
    "test": test,
    "tru": tru,
    "fal": fal,
    "insp_times": 0,
    "div_by": div_by
  }

  return monkeys

def execute_round(monkeys, total_monkeys):
  for i in range(total_monkeys):
    monkey = monkeys[str(i)]
    while(len(monkey["items"]) != 0):
      current_item = monkey["items"].pop(0)
      worry = monkey["operation"](current_item)
      worry = worry // 3
      if (monkey["test"](worry)):
        monkeys[str(monkey["tru"])]["items"].append(worry)
      else:
        monkeys[str(monkey["fal"])]["items"].append(worry)
      monkey["insp_times"] += 1
  return monkeys

def solution1(input):
  monkeys = {}
  total_monkeys = 0

  i = 0
  while (i < len(input)):
    line = input[i]
    if (line.startswith("Monkey")):
      monkeys = add_monkey(monkeys, input[i:i+6])
      total_monkeys += 1
    i += 1

  for i in range(20):
    monkeys = execute_round(monkeys, total_monkeys)
  #pprint.pprint(monkeys)

  ins_times = []
  for monkey in monkeys:
    ins_times.append(monkeys[str(monkey)]["insp_times"])

  ins_times.sort()
  return ins_times[-1] * ins_times[-2]

print("Example Solution 1:", solution1(example))
print("Solution 1:", solution1(real_input))

## Problem 2

def get_modulo(monkeys):
  div_by = []
  for monkey in monkeys:
    div_by.append(monkeys[str(monkey)]["div_by"])
  return np.lcm.reduce(div_by)

def execute_round2(monkeys, total_monkeys, modulo):
  for i in range(total_monkeys):
    monkey = monkeys[str(i)]
    while(len(monkey["items"]) != 0):
      current_item = monkey["items"].pop(0)
      worry = monkey["operation"](current_item)
      worry = worry % modulo
      if (monkey["test"](worry)):
        monkeys[str(monkey["tru"])]["items"].append(worry)
      else:
        monkeys[str(monkey["fal"])]["items"].append(worry)
      monkey["insp_times"] += 1
  return monkeys

def solution2(input):
  monkeys = {}
  total_monkeys = 0

  i = 0
  while (i < len(input)):
    line = input[i]
    if (line.startswith("Monkey")):
      monkeys = add_monkey(monkeys, input[i:i+6])
      total_monkeys += 1
    i += 1

  modulo = get_modulo(monkeys)
  for i in range(10000):
    monkeys = execute_round2(monkeys, total_monkeys, modulo)

  ins_times = []
  for monkey in monkeys:
    ins_times.append(monkeys[str(monkey)]["insp_times"])

  ins_times.sort()
  return ins_times[-1] * ins_times[-2]


print("Example Solution 2:", solution2(example))
print("Solution 2:", solution2(real_input))
