###                                              ###
###                                              ###
### TEMPLATE FOR READING THE INPUT/EXAMPLE TEXT  ###
###                                              ###
###                                              ###
import math

example = None
real_input = None

with open("example.txt") as f:
  example = [line.strip() for line in f.readlines()]

with open("input.txt") as f:
  real_input = [line.strip() for line in f.readlines()]


#print("EXAMPLE >>", example)
#print("INPUT >>", real_input)

class Cube:
  def __init__(self, x, y , z):
    self.x = x
    self.y = y
    self.z = z

  def __add__(self, other):
    return Cube(self.x + other.x, self.y + other.y, self.z + other.z)

  def __str__(self):
    return f"({self.x}, {self.y}, {self.z})"


def check_sides(cube, cubes):
  points = [Cube(1,0,0), Cube(-1,0,0), Cube(0,1,0), Cube(0,-1,0), Cube(0,0,1), Cube(0,0,-1)]

  sides = 6
  for point in points:
    p = cube + point
    if str(p) in cubes:
      sides -= 1
  return sides

def solution1(input):
  cubes_list = []
  cubes = set()
  for line in input:
    x = int(line.split(",")[0])
    y = int(line.split(",")[1])
    z = int(line.split(",")[2])
    cube = Cube(x, y, z)
    cubes_list.append(cube)
    cubes.add(str(cube))

  sides = 0
  for cube in cubes_list:
    sides += check_sides(cube, cubes)
  return sides

print("Example 1: ", solution1(example))
print("Solution 1: ", solution1(real_input))


def update_values(values, x, y, z):
  values["x"]["min"] = min(values["x"]["min"], x)
  values["y"]["min"] = min(values["y"]["min"], y)
  values["z"]["min"] = min(values["z"]["min"], z)

  values["x"]["max"] = max(values["x"]["max"], x)
  values["y"]["max"] = max(values["y"]["max"], y)
  values["z"]["max"] = max(values["z"]["max"], z)

  return values

def check_values(x, y, z, values):
  if x in range(values["x"]["min"] + 1, values["x"]["max"]):
    if y in range(values["y"]["min"] + 1, values["y"]["max"]):
      if z in range(values["z"]["min"] + 1, values["z"]["max"]):
        return True

  return False

def check_sides2(cube, cubes, values):
  points = [Cube(1,0,0), Cube(-1,0,0), Cube(0,1,0), Cube(0,-1,0), Cube(0,0,1), Cube(0,0,-1)]

  if (check_values(cube.x, cube.y, cube.z, values)):
    print(str(cube))
    return 0

  sides = 6
  for point in points:
    p = cube + point
    if str(p) in cubes:
      sides -= 1
  return sides

def solution2(input):
  cubes_list = []
  values = {
    "x": {
      "min": math.inf,
      "max": -math.inf
    },
    "y": {
      "min": math.inf,
      "max": -math.inf
    },
    "z": {
      "min": math.inf,
      "max": -math.inf
    }
  }
  cubes = set()
  for line in input:
    x = int(line.split(",")[0])
    y = int(line.split(",")[1])
    z = int(line.split(",")[2])
    cube = Cube(x, y, z)
    values = update_values(values, x, y, z)
    cubes_list.append(cube)
    cubes.add(str(cube))

  sides = 0
  print(values)
  for cube in cubes_list:
    sides += check_sides2(cube, cubes, values)
  return sides


print("Example 2: ", solution2(example))
