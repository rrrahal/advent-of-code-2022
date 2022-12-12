from collections import defaultdict
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


#print("EXAMPLE >>", example)
#print("INPUT >>", real_input)

class Node:
  def __init__(self, value, line, column):
    self.value = value
    self.up = None
    self.down = None
    self.right = None
    self.left = None
    self.id = str((line, column))

  def get_value(self):
    return self.value

  def set_up(self, node):
    self.up = node

  def set_down(self, node):
    self.down = node

  def set_left(self, node):
    self.left = node

  def set_right(self, node):
    self.right = node

  def __str__(self):
    return self.get_id()


    return f"value: {self.value}, up: {top}, down: {down}, left: {left}, right: {right}"

  def get_id(self):
    return self.id

  def get_neighboors(self):
    neighboors = []
    if self.up:
      neighboors.append(self.up)
    if self.down:
      neighboors.append(self.down)
    if self.right:
      neighboors.append(self.right)
    if self.left:
      neighboors.append(self.left)
    return neighboors


def possible_path(current_node, other_node):
  return other_node.get_value() - current_node.get_value() <= 1

def build_connections(matrix, i, j, number_of_lines, number_of_columns):
  if (is_index_in_matrix(i-1, j, number_of_lines, number_of_columns) and possible_path(matrix[i][j], matrix[i-1][j])):
    matrix[i][j].set_up(matrix[i-1][j])

  if (is_index_in_matrix(i+1,j, number_of_lines, number_of_columns) and possible_path(matrix[i][j], matrix[i+1][j])):
    matrix[i][j].set_down(matrix[i+1][j])

  if (is_index_in_matrix(i,j+1, number_of_lines, number_of_columns) and possible_path(matrix[i][j], matrix[i][j+1])):
    matrix[i][j].set_right(matrix[i][j+1])

  if (is_index_in_matrix(i,j-1, number_of_lines, number_of_columns) and possible_path(matrix[i][j], matrix[i][j-1])):
    matrix[i][j].set_left(matrix[i][j-1])

def is_index_in_matrix(i, j, number_of_lines, number_of_columns):
  if (i >= 0 and i < number_of_lines):
    if (j >= 0 and j < number_of_columns):
      return True
  return False

def build_graph(matrix):
  number_of_lines = len(matrix)
  number_of_columns = len(matrix[0])

  initial_node = None
  target_node = None

  for line in range(number_of_lines):
    for column in range(number_of_columns):
      element = matrix[line][column]
      if (element == "S"):
        node = Node(ord("a") - 96, line, column)
        initial_node = node
      elif(element == "E"):
        node = Node(ord("z") - 96, line, column)
        target_node = node
      else:
        node = Node(ord(element) - 96, line, column)
      matrix[line][column] = node

  for line in range(number_of_lines):
    for column in range(number_of_columns):
      build_connections(matrix, line, column, number_of_lines, number_of_columns)

  return initial_node, target_node

def a_star(start, goal):
  open = [start]

  cameFrom = {}

  g_score = defaultdict(lambda: math.inf)
  g_score[start.get_id()] = 0

  f_score = defaultdict(lambda: math.inf)
  f_score[start.get_id()] = 0

  while len(open) != 0:
    current = min(open, key = lambda x: g_score[x.get_id()])
    if current == goal:
      return g_score[current.get_id()]

    open.remove(current)

    for neighboor in current.get_neighboors():
      tentative_g_score = g_score[current.get_id()] + 1
      if tentative_g_score < g_score[neighboor.get_id()]:
        cameFrom[neighboor.get_id()] = current
        g_score[neighboor.get_id()] = tentative_g_score
        f_score[neighboor.get_id()] = tentative_g_score + 0 # we should have an H function
        if neighboor not in open:
          open.append(neighboor)

  return math.inf

def build_graph_with_as(matrix):
  number_of_lines = len(matrix)
  number_of_columns = len(matrix[0])
  As = []

  initial_node = None
  target_node = None

  for line in range(number_of_lines):
    for column in range(number_of_columns):
      element = matrix[line][column]
      if (element == "S"):
        node = Node(ord("a") - 96, line, column)
        initial_node = node
        As.append(node)
      elif(element == "E"):
        node = Node(ord("z") - 96, line, column)
        target_node = node
      elif(element == "a"):
        node = Node(ord(element) - 96, line, column)
        As.append(node)
      else:
        node = Node(ord(element) - 96, line, column)
      matrix[line][column] = node

  for line in range(number_of_lines):
    for column in range(number_of_columns):
      build_connections(matrix, line, column, number_of_lines, number_of_columns)

  return initial_node, target_node, As

def solution1(input):
  matrix = [ list(line) for line in input ]
  start, goal = build_graph(matrix)
  result = a_star(start, goal)
  return result

print("Example 1: ", solution1(example))
print("Solution 1:", solution1(real_input))

## Problem 2

def solution2(input):
  paths = []
  matrix = [ list(line) for line in input ]
  start, goal, As = build_graph_with_as(matrix)

  for a in As:
    paths.append(a_star(a, goal))

  return min(paths)


print("Example 2: ", solution2(example))
print("Solution 2:", solution2(real_input))
