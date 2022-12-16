import math
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

  def distance(self, other):
    return abs(self.x - other.x) + abs(self.y - other.y)

  def impossible_points(self, d, column):
    dist_until_column = self.distance(Point(self.x, column))
    if (dist_until_column > d):
      return []
    if(dist_until_column == d):
      return [Point(self.x, column)]
    else:
      points = []
      min_x = self.x - (d - dist_until_column)
      max_x = self.x + (d - dist_until_column) + 1
      for i in range(min_x, max_x):
        points.append(Point(i, column))
      return points

  def x(self):
    return self.x

  def y(self):
    return self.y

def get_point(string):
  x = int(string.split(",")[0].split("=")[1])
  y = int(string.split(",")[1].split("=")[1])
  return Point(x, y)

def get_points(line):
  line = line.split(":")
  sensor = get_point(line[0])
  beacon = get_point(line[1])
  return sensor, beacon



def solution1(input, column):
  impossible_points = set()
  beacons = set()
  for line in input:
    sensor, beacon = get_points(line)
    distance = sensor.distance(beacon)
    beacons.add(str(beacon))
    if str(beacon) in impossible_points:
      impossible_points.remove(str(beacon))

    points = sensor.impossible_points(distance, column)
    for point in points:
      if str(point) not in beacons:
        impossible_points.add(str(point))

  return len(impossible_points)

#print("Example 1 ->", solution1(example, 10))
#print("Solution 1 ->", solution1(real_input, 2000000))

## Problem 2

def solution2(input, max_value):
  impossible_points = set()
  beacons = set()
  covered_y = []
  for line in input:
    sensor, beacon = get_points(line)
    distance = sensor.distance(beacon)
    beacons.add(str(beacon))
    for y in range(sensor.y - distance, sensor.y + distance + 1):
      covered_y.append(y)
  min_y = min(covered_y)
  max_y = max(covered_y)
  possible_y = []
  for y in range(min_y, max_y):
    if y not in covered_y:
      possible_y.append(y)
  print(possible_y)


print("Example 2 ->", solution2(example, 20))
print("Solution 2:", solution2(real_input, 4000000))
