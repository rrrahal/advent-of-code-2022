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

class CircularArray:
  def __init__(self, array):
    self.list = array
    self.index = 0
    self.len = len(self.list)

  def next(self):
    if self.index == self.len:
      self.index = 0
    element = self.list[self.index]
    self.index += 1
    return element


def get_initial_position(shape, tallest_rock):
  positions = []
  y_position = tallest_rock + 4
  for position in shape:
    p = Point(position.x, position.y + y_position)
    positions.append(Point(position.x, position.y + y_position))

  return positions

def pos_in_rocks(position, rocks_position):
  for coord in position:
    if str(coord) in rocks_position:
      return True
    if coord.y <= 0:
      return True
  return False

def movement(position, commands, apply_command, rocks_position):
  p = None
  command = None
  can_go_right = True
  can_go_left = True
  for pos in position:
    if pos.x == 6:
      can_go_right = False
    elif pos.x == 0:
      can_go_left = False

  if apply_command:
    command = commands.next()
    if command == ">" and can_go_right:
      p = Point(1,0)
      for pos in position:
        if (str(pos + p) in rocks_position):
          p = Point(0,0)
    elif command == "<" and can_go_left:
      p = Point(-1,0)
      for pos in position:
        if (str(pos + p) in rocks_position):
          p = Point(0,0)
    else:
      p = Point(0,0)
  else:
    p = Point(0,-1)

  new_pos = []

  for pos in position:
    coord = pos + p
    if coord.x < 0:
      coord = Point(0, coord.y)
    elif coord.x > 6:
      coord = Point(6, coord.y)
    new_pos.append(coord)

  return new_pos

def move(rocks_position, tallest_rock, shape, commands):
  position = get_initial_position(shape, tallest_rock)
  next_position = position
  apply_command = True

  while(not pos_in_rocks(next_position, rocks_position)):
    position = next_position
    next_position = movement(position, commands, apply_command, rocks_position)
    apply_command = not apply_command


  for coord in position:
    rocks_position.add(str(coord))
    if coord.y > tallest_rock:
      tallest_rock = coord.y

  return rocks_position, tallest_rock

def draw(rocks, tallest_rock):
  for i in range(tallest_rock + 4, 0, -1):
    s = "|"
    for j in range(7):
      if str(Point(j, i)) in rocks:
        s += "#"
      else:
        s += "."
    print(s + "|")


def solution1(input):
  rocks_position = set()
  tallest_rock = 0
  hori_shape = [Point(2,0), Point(3,0), Point(4,0), Point(5,0)]
  plus_shape = [Point(3,2), Point(3,1), Point(2,1), Point(4,1), Point(3,0)]
  l_shape = [Point(4,2), Point(4,1), Point(4,0), Point(3,0), Point(2,0)]
  tower_shape = [Point(2,0), Point(2,1), Point(2,2), Point(2,3)]
  sq_shape = [Point(2,0), Point(2,1), Point(3,0), Point(3,1)]
  shapes = CircularArray([hori_shape, plus_shape, l_shape, tower_shape, sq_shape])

  print(input)
  number_of_rocks = 0
  commands = CircularArray(input[0])
  while (number_of_rocks < 2022):
    rocks_position, tallest_rock = move(rocks_position, tallest_rock, shapes.next(), commands)
    number_of_rocks += 1
  return tallest_rock

#print("EXAMPLE >>", example)
#print("INPUT >>", real_input)

#print("Example 1 ->", solution1(example))
#print("Solution 1 ->", solution1(real_input))


def get_final_value(state, max_value, tallest_rock, number_of_rocks, rocks_map):
  n_r = number_of_rocks - state["number_of_rocks"]
  t_r = tallest_rock - state["tallest_rock"]

  final_v = (max_value // n_r) * t_r
  remaining = rocks_map[str(state["number_of_rocks"] + (max_value % n_r))]
  for i in range(state["number_of_rocks"] + (max_value % n_r) - 3, state["number_of_rocks"] + (max_value % n_r) + 3):
    print(i, rocks_map[str(i)])
  print("\n")
  print("real i:", state["number_of_rocks"] + (max_value % n_r))



  return final_v + remaining - state["tallest_rock"]


def solution2(input, max_value):
  rocks_position = set()
  tallest_rock = 0
  hori_shape = [Point(2,0), Point(3,0), Point(4,0), Point(5,0)]
  plus_shape = [Point(3,2), Point(3,1), Point(2,1), Point(4,1), Point(3,0)]
  l_shape = [Point(4,2), Point(4,1), Point(4,0), Point(3,0), Point(2,0)]
  tower_shape = [Point(2,0), Point(2,1), Point(2,2), Point(2,3)]
  sq_shape = [Point(2,0), Point(2,1), Point(3,0), Point(3,1)]
  shapes = CircularArray([hori_shape, plus_shape, l_shape, tower_shape, sq_shape])
  states = {}
  rocks_map = {}

  number_of_rocks = 0
  commands = CircularArray(input[0])
  while (number_of_rocks < max_value):
    rocks_position, tallest_rock = move(rocks_position, tallest_rock, shapes.next(), commands)
    number_of_rocks += 1

    s = ""
    for i in range(7):
      p = Point(i, tallest_rock)
      if str(p) in rocks_position:
        s += "X"
      else:
        s += "."
    s += " " + str(commands.index) + str(shapes.index)
    if s in states:
      return get_final_value(states[s], max_value, tallest_rock, number_of_rocks, rocks_map)
    else:
      states[s] = {"tallest_rock" : tallest_rock, "number_of_rocks": number_of_rocks}
      rocks_map[str(number_of_rocks)] = tallest_rock
  return tallest_rock

print("Example 2 ->", solution2(example, 1000000000000))
print("Solution 2 ->", solution2(real_input, 1000000000000))
