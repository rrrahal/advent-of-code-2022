###                                              ###
###                                              ###
### TEMPLATE FOR READING THE INPUT/EXAMPLE TEXT  ###
###                                              ###
###                                              ###

example = None
real_input = None
from functools import cache


with open("example.txt") as f:
  example = [line.strip() for line in f.readlines()]

with open("input.txt") as f:
  real_input = [line.strip() for line in f.readlines()]


#print("EXAMPLE >>", example)
#print("INPUT >>", real_input)

def parse_input(input):
  elves = {}
  for line in input:
    elf = line.split(": ")[0]
    operation = line.split(": ")[1].split(" ")
    if len(operation) == 1:
      elves[elf] = {
        "value": int(operation[0]),
        "initial": True
      }
    else:
      elves[elf] = {
        "operation": operation,
        "initial": False
      }

  return elves

#@cache
def get_value(name, elves):
  elf = elves[name]
  if elf["initial"]:
    return elf["value"]

  else:
    left_v = get_value(elf["operation"][0], elves)
    op = elf["operation"][1]
    right_v = get_value(elf["operation"][2], elves)
    elves[elf["operation"][0]] = {
      "initial": True,
      "value": left_v
    }
    elves[elf["operation"][2]] = {
      "initial": True,
      "value": right_v
    }
    return eval(f"{left_v} {op} {right_v}")

def get_string(name, elves):
  elf = elves[name]
  if elf["initial"]:
    return elf["value"]

  else:
    left_v = get_string(elf["operation"][0], elves)
    op = elf["operation"][1]
    right_v = get_string(elf["operation"][2], elves)
    elves[elf["operation"][0]] = {
      "initial": True,
      "value": left_v
    }
    elves[elf["operation"][2]] = {
      "initial": True,
      "value": right_v
    }
    if "x" in str(left_v) or "x" in str(right_v):
      return f"({left_v} {op} {right_v})"
    return eval(f"({left_v} {op} {right_v})")

def solution1(input):
  elves = parse_input(input)
  #print(elves)
  return get_value('root', elves)

#print("Example 1 ->", solution1(example))
#print("Solution 1 ->", solution1(real_input))


def solution2(input):
  elves = parse_input(input)
  elves["humn"] = {
    "value": "x",
    "initial": True
  }
  left = get_string(elves['root']["operation"][0], elves)
  right = get_string(elves['root']["operation"][2], elves)
  print(f"{left} = {right}")
  expr = f"{left} - {right}"
  grouped = eval(expr.replace("x",'1j'))
  return -grouped.real/grouped.imag



print("Example 2 ->", solution2(example))
print("Solution 2 ->", solution2(real_input))
