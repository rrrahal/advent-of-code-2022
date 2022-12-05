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



def is_overlap(sfirst, efirst, ssecond, esecond):
  # first in whitin the second
  if (sfirst - ssecond <= 0 and efirst - esecond >= 0):
    #print("Is Overlap: ", sfirst, efirst, ssecond, esecond)
    return True
  if (ssecond - sfirst <= 0 and esecond - efirst >= 0):
    #print("Is Overlap: ", sfirst, efirst, ssecond, esecond)
    return True
  return False

def not_overlap(sfirst, efirst, ssecond, esecond):
  if(efirst < ssecond):
    return True
  if (esecond < sfirst):
    return True
  return False


def solution1(pairs):
  total_overlap = 0
  for pair in pairs:
    [f, s] = pair.split(",")
    f = f.split("-")
    s = s.split("-")
    if is_overlap(int(f[0]), int(f[1]), int(s[0]), int(s[1])):
      total_overlap += 1
  return total_overlap


def solution2(pairs):
  total_overlap = 0
  for pair in pairs:
    [f, s] = pair.split(",")
    f = f.split("-")
    s = s.split("-")
    if not not_overlap(int(f[0]), int(f[1]), int(s[0]), int(s[1])):
      total_overlap += 1
  return total_overlap



print("Example Solution 1: ", solution1(example))
print("Solution 1: ", solution1(real_input))


print("Example Solution 2: ", solution2(example))
print("Solution 2: ", solution2(real_input))
