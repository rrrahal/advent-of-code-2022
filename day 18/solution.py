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


def check_sides2(cube, cubes):
  points = [Cube(1,0,0), Cube(-1,0,0), Cube(0,1,0), Cube(0,-1,0), Cube(0,0,1), Cube(0,0,-1)]

  sides = 6
  for point in points:
    p = cube + point
    if str(p) in cubes:
      sides -= 1
  return sides

def solution2(input):
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


print("Example 2: ", solution2(example))
