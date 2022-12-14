import ast
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


def compare_items(item1, item2):
  if isinstance(item1, int) and isinstance(item2, int):
    if item1 < item2:
      return True
    elif item1 > item2:
      return False
    return None

  if isinstance(item1, list) and isinstance(item2, int):
    return compare_arrays(item1, [item2])

  if isinstance(item1, int) and isinstance(item2, list):
    return compare_arrays([item1], item2)

  return compare_arrays(item1, item2)

def compare_arrays(array1, array2):
  size1 = len(array1)
  size2 = len(array2)

  for i in range(size1):
    if i >= size2:
      return False
    result = compare_items(array1[i], array2[i])
    if result is False:
      return False
    if result is True:
      return True
  if size1 == size2:
    return None
  return True

def solution1(input):
  items_index = 1
  total_sum = 0
  for i in range(len(input)):
    if input[i] == '':
      array1 = ast.literal_eval(input[i-2])
      array2 = ast.literal_eval(input[i-1])
      result = compare_arrays(array1, array2)
      if (result):
        total_sum += items_index
      items_index += 1

  return total_sum

#print("Example 1 ->", solution1(example))
#print("Solution 1: ", solution1(real_input))

def insertion_sort(packet_order, item):
  for i in range(len(packet_order)):
    if (compare_arrays(item, packet_order[i]) == True):
      packet_order.insert(i, item)
      return i
  packet_order.append(item)
  return len(packet_order) - 1


def solution2(input):
  packet_order = []
  for i in range(len(input)):
    if input[i] != '':
      array = ast.literal_eval(input[i])
      insertion_sort(packet_order, array)

  index_1 = insertion_sort(packet_order, [[2]]) + 1
  index_2 = insertion_sort(packet_order, [[6]]) + 1
  for item in packet_order:
    print(item)
  return index_1 * index_2


print("Example 2 ->", solution2(example))
print("Solution 2 ->", solution2(real_input))
