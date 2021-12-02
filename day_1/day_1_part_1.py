with open("input.txt") as file:
  lines = file.readlines()

lines = [x.strip() for x in lines]

times_increased = 0
prev_depth = None

for depth in lines:
  if prev_depth is not None:
    if int(prev_depth) < int(depth):
      times_increased += 1
  prev_depth = depth

print("Times increased:", times_increased)