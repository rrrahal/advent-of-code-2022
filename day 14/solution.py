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

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __sub__(self, other):
    return Point(self.x - other.x, self.y - other.y)

  def __add__(self, other):
    return Point(self.x + other.x, self.y + other.y)

  def __str__(self):
    return f"({self.x}, {self.y})"

  def get_x(self):
    return self.x

  def get_y(self):
    return self.y

def add_rocks(start, end, rocks):
  distance = end - start
  if (distance.get_x() < 0 or distance.get_y() < 0):
    return add_rocks(end, start, rocks)

  for i in range(distance.get_y() + 1):
    new_rock = start + Point(0, i)
    rocks.add(str(new_rock))

  for i in range(distance.get_x() + 1):
    new_rock = start + Point(i, 0)
    rocks.add(str(new_rock))

  return rocks

def get_point(point):
  point = point.split(",")
  x = int(point[0])
  y = int(point[1])
  return Point(x, y)


def add_sand(rocks, sand, last_rock, start_pos):
  if start_pos.get_y() > last_rock:
    return rocks, sand

  down = start_pos + Point(0,1)
  if (str(down) not in rocks and str(down) not in sand):
    return add_sand(rocks, sand, last_rock, down)

  left_down = start_pos + Point(-1, 1)
  if (str(left_down) not in rocks and str(left_down) not in sand):
    return add_sand(rocks, sand, last_rock, left_down)

  right_down = start_pos + Point(1,1)
  if (str(right_down) not in rocks and str(right_down) not in sand):
    return add_sand(rocks, sand, last_rock, right_down)

  sand.add(str(start_pos))
  return rocks, sand


def solution1(input):
  rocks = set()
  sand = set()
  last_rock = 0
  for line in input:
    points = line.split(" -> ")
    for i in range(1, len(points)):
      start = get_point(points[i-1])
      end = get_point(points[i])
      last_rock = max(last_rock, start.get_y(), end.get_y())
      rocks = add_rocks(start, end, rocks)

  last_sand_len = -1
  while(len(sand) > last_sand_len):
    last_sand_len = len(sand)
    rocks, sand = add_sand(rocks, sand, last_rock, Point(500,0))
  print(len(sand))

  return len(sand)


print("Example 1 ->", solution1(example))
print("Solution 1 ->", solution1(real_input))

def in_rocks(point, rocks, floor_level):
  return str(point) in rocks or point.get_y() == floor_level

def add_sand(rocks, sand, floor_level, start_pos):
  down = start_pos + Point(0,1)
  if not in_rocks(down, rocks, floor_level) and str(down) not in sand:
    return add_sand(rocks, sand, floor_level, down)

  left_down = start_pos + Point(-1, 1)
  if not in_rocks(left_down, rocks, floor_level) and str(left_down) not in sand:
    return add_sand(rocks, sand, floor_level, left_down)

  right_down = start_pos + Point(1,1)
  if not in_rocks(right_down, rocks, floor_level) and str(right_down) not in sand:
    return add_sand(rocks, sand, floor_level, right_down)

  sand.add(str(start_pos))
  print(str(start_pos))
  return rocks, sand

def solution2(input):
  rocks = set()
  sand = set()
  last_rock = 0
  for line in input:
    points = line.split(" -> ")
    for i in range(1, len(points)):
      start = get_point(points[i-1])
      end = get_point(points[i])
      last_rock = max(last_rock, start.get_y(), end.get_y())
      rocks = add_rocks(start, end, rocks)
  floor_level = last_rock + 2
  while(str(Point(500,0)) not in sand):
    rocks, sand = add_sand(rocks, sand, floor_level, Point(500,0))
  return len(sand)

print("Example 2 ->", solution2(example))
print("Solution 2", solution2(real_input))
