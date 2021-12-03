with open("input.txt") as file:
  lines = file.readlines()

lines = [x.strip() for x in lines]

times_increased = 0

for index, depth in enumerate(lines):
  if index >= 2 and index < len(lines) - 1:
    prevMeasurement = int(lines[index - 2]) + int(lines[index - 1]) + int(lines[index])
    currMeasurement = int(lines[index - 1]) + int(lines[index]) + int(lines[index + 1])
    if prevMeasurement < currMeasurement:
      times_increased += 1

print("Times increased:", times_increased)