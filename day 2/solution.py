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

oponent_play = {
  "A": "rock",
  "B": "paper",
  "C": "scissors"
}

my_play = {
  "X": "rock",
  "Y": "paper",
  "Z": "scissors"
}

play_score = {
  "rock": 1,
  "paper": 2,
  "scissors": 3
}

game_score = {
  "l": 0,
  "w": 6,
  "d": 3
}

### PART 1

def game_result(oponent_choice, my_choice):
  a = oponent_play[oponent_choice]
  b = my_play[my_choice]
  if (a == b):
    return "d"
  if (a == 'rock' and b == "paper"):
    return "w"
  if (a == "paper" and b == "scissors"):
    return "w"
  if (a == "scissors" and b == "rock"):
    return "w"
  return "l"


def get_total_score(plays):
  total_score = 0
  for play in plays:
    [a, b] = play.split()
    total_score += game_score[game_result(a, b)] + play_score[my_play[b]]
  return total_score



print("Example Solution 1: ", get_total_score(example))
print("Solution 1: ", get_total_score(real_input))


## Part 2

expected_output = {
  "X": "l",
  "Y": "d",
  "Z": "w"
}

def get_expected_play(oponent_choice, result):
  if (result == "d"):
    return oponent_choice
  if (result == "w"):
    if (oponent_choice == "rock"):
      return "paper"
    if (oponent_choice == "paper"):
      return "scissors"
    if (oponent_choice == "scissors"):
      return "rock"
  else:
    if (oponent_choice == "rock"):
      return "scissors"
    if (oponent_choice == "paper"):
      return "rock"
    if (oponent_choice == "scissors"):
      return "paper"


def get_total_score_part2(plays):
  total_score = 0
  for play in plays:
    [a, b] = play.split()
    expected = expected_output[b]
    opo_play = oponent_play[a]
    total_score += game_score[expected] + play_score[get_expected_play(opo_play, expected)]
  return total_score


print("Example Solution 2: ", get_total_score_part2(example))
print("Solution 2: ", get_total_score_part2(real_input))
