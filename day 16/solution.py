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
  valves = {
  }

  for line in input:
    valve = line.split("Valve ")[1][:2]
    rate = line.split("=")[1].split(";")[0]
    valves[valve] = {}
    valves[valve]["rate"] = int(rate)
    paths = []
    s = line.split("; ")[1]
    for i in range(len(s)):
      if (s[i].isupper()):
        paths = s[i:]
        break
    paths = [path.strip() for path in paths.split(",")]
    valves[valve]["paths"] = paths

  broken_valves = set()
  func_valves = {}
  for valve in valves:
    if valves[valve]["rate"] == 0:
      broken_valves.add(valve)
    else:
      func_valves[valve] = valves[valve]["rate"]

  print(broken_valves)
  print(func_valves)




print("Example 1 ->", solution1(example))
