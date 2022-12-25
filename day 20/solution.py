###                                              ###
###                                              ###
### TEMPLATE FOR READING THE INPUT/EXAMPLE TEXT  ###
###                                              ###
###                                              ###
from copy import copy

example = None
real_input = None

with open("example.txt") as f:
  example = [line.strip() for line in f.readlines()]

with open("input.txt") as f:
  real_input = [line.strip() for line in f.readlines()]


#print("EXAMPLE >>", example)
#print("INPUT >>", real_input)

class Number:
  def __init__(self, val):
    self.val = val


class CircularList:
  def __init__(self, list):
    self.list = list
    self.size = len(list)

  def __getitem__(self, index):
    return self.list[index % self.size]

  def __str__(self) -> str:
    lis = []
    for item in self.list:
      lis.append(item.val)
    return str(lis)

  def find(self, item):
    return self.list.index(item)

  def move(self, index):
    item_to_move = self.list[index].val

    offset = abs(item_to_move) % (self.size - 1)
    offset = -offset if item_to_move < 0 else offset
    pos = index + offset
    if pos >= self.size:
        pos = pos % self.size + 1
    elif pos == 0:
        pos = 0 if offset >= 0 else self.size
    popped = self.list.pop(index)
    self.list.insert(pos, popped)


def solution(input):
  arr = []
  zero = None
  for i in range(len(input)):
    line = input[i]
    number = Number(int(line[0:]))
    arr.append(number)
    if (int(line[0:]) == 0):
      zero = number
  circular_list = CircularList(copy(arr))
  for i in range(len(arr)):
    item = arr[i]
    index = circular_list.find(item)
    circular_list.move(index)

  sum = 0
  zero_index = circular_list.find(zero)

  for i in [1000, 2000, 3000]:
        index = zero_index + i % len(arr)
        index = index % len(arr)
        sum += circular_list[index].val

  return sum

print("Example 1 ->", solution(example))
print("Solution 1 ->", solution(real_input))


def solution2(input):
  arr = []
  zero = None
  for i in range(len(input)):
    line = input[i]
    number = Number(int(line[0:]) * 811589153)
    arr.append(number)
    if (int(line[0:]) == 0):
      zero = number
  circular_list = CircularList(copy(arr))

  for i in range(10):
    for i in range(len(arr)):
      item = arr[i]
      index = circular_list.find(item)
      circular_list.move(index)
  print(str(circular_list))

  sum = 0
  zero_index = circular_list.find(zero)

  for i in [1000, 2000, 3000]:
        index = zero_index + i % len(arr)
        index = index % len(arr)
        sum += circular_list[index].val

  return sum

print("Example 2 ->", solution2(example))
print("Solution 2 ->", solution2(real_input))
