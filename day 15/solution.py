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

  def get_fronteirs(self, distance, max_value):
    top_point = Point(self.x, self.y + distance + 1)
    points = [top_point]
    p = top_point
    while(p.y >= self.y):
      p = p + Point(1, -1)
      if (p.x > 0 and p.x <= max_value):
        if (p.y > 0 and p.y <= max_value):
          points.append(p)

    p = top_point
    while(p.y >= self.y):
      p = p + Point(-1, -1)
      if (p.x > 0 and p.x <= max_value):
        if (p.y > 0 and p.y <= max_value):
          points.append(p)

    bottom_point = Point(self.x, self.y - distance - 1)
    points.append(bottom_point)
    p = bottom_point

    while(p.y <= self.y):
      p = p + Point(1, 1)
      if (p.x > 0 and p.x <= max_value):
        if (p.y > 0 and p.y <= max_value):
          points.append(p)

    p = bottom_point

    while(p.y <= self.y):
      p = p + Point(-1, 1)
      if (p.x > 0 and p.x <= max_value):
        if (p.y > 0 and p.y <= max_value):
          points.append(p)
    return points

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

def inside_sensors(sensors, point, max_value):
  if point.x > max_value or point.y > max_value:
    return True
  if point.x < 0 or point.y < 0:
    return True
  for sensor in sensors:
    if sensor.distance(point) <= sensors[sensor]:
      return True
  return False


def solution2(input, max_value):
  sensors = {}
  beacons = set()
  fronteirs = []
  i = 0
  for line in input:
    i += 1
    print("starting sensor", i, "of ", len(input))
    sensor, beacon = get_points(line)
    distance = sensor.distance(beacon)
    sensors[sensor] = distance
    beacons.add(str(beacon))
    fronteirs.append(sensor.get_fronteirs(distance, max_value))

  i = 0
  for fronteir in fronteirs:
    i += 1
    print("starting fronteir", i, "of ", len(fronteirs))
    for point in fronteir:
      if (not inside_sensors(sensors, point, max_value)):
        return (point.x * 4000000) + point.y
  return None

#print("Example 2 ->", solution2(example, 20))
print("Solution 2:", solution2(real_input, 4000000))
