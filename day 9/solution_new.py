import copy

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


with open("example_2.txt") as f:
  example2 = [line.strip() for line in f.readlines()]


#print("EXAMPLE >>", example)
#print("INPUT >>", real_input)

## Problem 1

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __add__(self, other):
    return Point(self.x + other.x, self.y + other.y)

  def __sub__(self, other):
    return Point(self.x - other.x, self.y - other.y)

  def get_tuple(self):
    return (self.x, self.y)

  def same(self, other):
    if (self.x == other.x and self.y == other.y):
      return True
    return False

  def within_one(self, other):
    if (abs(self.x - other.x) < 2 and abs(self.y - other.y) < 2):
      return True
    return False

  def __repr__(self):
    return f"({self.x}, {self.y})"

  def __str__(self):
    return f"({self.x}, {self.y})"

  def get_follow_move(self, other):
    if(self.x == other.x):
      if (self.y > other.y):
        return Point(0,1)
      return Point(0, -1)

    if(self.y == other.y ):
      if (self.x > other.x):
        return Point(1,0)
      return Point(-1, 0)

    if (self.x > other.x):
      if (self.y > other.y):
        return Point(1,1)
      return Point(1, -1)
    else:
      if (self.y > other.y):
        return Point(-1,1)
      return Point(-1, -1)



def direction_to_coordinate(direction):
  if direction == "U":
    return Point(0, 1)
  if direction == "D":
    return Point(0, -1)
  if direction == "R":
    return Point(1, 0)
  if direction == "L":
    return Point(-1,0)
  else:
    return Point(0,0)

def coordinate_to_direction(coordinate):
  tup = coordinate.get_tuple()
  if tup == (0, 1):
    return "U"
  if tup == (0, -1):
    return "D"
  if tup == (1, 0):
    return "R"
  if tup == (-1, 0):
    return "L"
  return "N"

def move(current_head_position, tail_position, direction):
  new_head_position = current_head_position + direction_to_coordinate(direction)
  if (new_head_position.within_one(tail_position)):
    return new_head_position, tail_position

  if (new_head_position.same(tail_position)):
    return new_head_position, tail_position

  else:
    return new_head_position, current_head_position

def solution1(input):
  head_position = Point(0,0)
  tail_position = Point(0,0)
  tail_visited = set()
  tail_visited.add(str(tail_position))

  for instruction in input:
    instruction = instruction.split()
    direction = instruction[0]
    value = int(instruction[1])
    for _ in range(value):
      head_position, tail_position = move(head_position, tail_position, direction)
      tail_visited.add(str(tail_position))

  #print(tail_visited)
  return len(tail_visited)

#print("Example 1: Solution 1:", solution1(example))
#print("Solution 1:", solution1(real_input))

def follow(head, tail):
  if (head.within_one(tail)):
    return head, tail
  if (head.same(tail)):
    return head, tail

  follow_move = head.get_follow_move(tail)
  return head, tail + follow_move


def solution2(input):
  knots = [Point(0,0) for _ in range(10)]
  tail_visited = set()
  tail_visited.add(str(knots[-1]))

  for instruction in input:
    instruction = instruction.split()
    direction = instruction[0]
    value = int(instruction[1])
    for _ in range(value):
      head, tail = move(knots[0], knots[1], direction)
      knots[0] = head
      knots[1] = tail
      for i in range(1,len(knots) - 1):
        head, tail = follow(knots[i], knots[i+1])
        knots[i+1] = tail
      tail_visited.add(str(knots[-1]))

  return len(tail_visited)

print("Example: Solution 2:", solution2(example2))
print("Solution 2:", solution2(real_input))
