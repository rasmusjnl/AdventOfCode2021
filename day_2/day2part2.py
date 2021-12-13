with open("input.txt") as file:
  lines = file.readlines()

lines = [x.strip() for x in lines]

aim = 0
depth = 0
horizontal = 0

for line in lines:
  split_line = line.split()
  type = split_line[0]
  value = int(split_line[1])
  if type == "forward":
    horizontal += value
    depth += aim * value
  elif type == "up":
    aim -= value
  elif type == "down":
    aim += value

print("answer:", depth * horizontal)