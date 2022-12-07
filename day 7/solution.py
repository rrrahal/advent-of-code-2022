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


## Problem 1

next_ls = []

def process_cd(current_dir, command):
  target = command[3:]
  if (target == ".."):
    current_dir.pop()
  else:
    current_dir.append(target)

  return current_dir

def process_ls(directories, output, current_dir):
  full_path = "".join(current_dir)
  directory = full_path

  if directory in directories:
    return directories

  ls_commands = []
  i = 0
  while(i < len(output) and not output[i].startswith("$")):
    ls_commands.append(output[i])
    i += 1

  directories[directory] = {
    "size": 0,
    "contains": []
  }

  for line in ls_commands:
    if line.startswith("dir"):
      target = line[4:]
      directories[directory]["contains"].append(full_path + target)
    else:
      target = line.split()[0]
      directories[directory]["size"] += int(target)


  return directories

def get_true_size(directories, dir):
  total_size = directories[dir]["size"]
  for other in directories[dir]["contains"]:
    total_size += get_true_size(directories, other)

  return total_size

def solution1(output):
  current_dir = []
  directories = {}

  for i in range(len(output)):
    command = output[i]
    if command.startswith("$ cd"):
      current_dir = process_cd(current_dir, command[2:])
    elif command.startswith("$ ls"):
      directories = process_ls(directories, output[i+1:], current_dir)


  true_sizes = {}
  for dir in directories:
    true_sizes[dir] = get_true_size(directories, dir)

  final_sum = 0
  for dir in true_sizes:
    if true_sizes[dir] <= 100000:
      final_sum += true_sizes[dir]

  return final_sum


## Problem 2

def get_true_sizes(output):
  current_dir = []
  directories = {}

  for i in range(len(output)):
    command = output[i]
    if command.startswith("$ cd"):
      current_dir = process_cd(current_dir, command[2:])
    elif command.startswith("$ ls"):
      directories = process_ls(directories, output[i+1:], current_dir)


  true_sizes = {}
  for dir in directories:
    true_sizes[dir] = get_true_size(directories, dir)

  return true_sizes

def solution2(output):
  true_sizes = get_true_sizes(output)

  TOTAL_DISK_SPACE = 70000000
  NEEDED_SPACE = 30000000

  current_used_space = true_sizes["/"]

  needed_unused_space = NEEDED_SPACE - (TOTAL_DISK_SPACE - current_used_space)

  best_dir = None
  min_space = -70000000

  possible_dirs = []

  for dir in true_sizes:
    left = needed_unused_space - true_sizes[dir]
    if (left < 0 and left > min_space):
      possible_dirs.append(true_sizes[dir])

  return sorted(possible_dirs)[0]




#print("Example Solution 1: ", solution1(example))
#print("Solution 1: ", solution1(real_input))

print("Example Solution 2: ", solution2(example))
print("Solution 2: ", solution2(real_input))
