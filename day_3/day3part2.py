from collections import Counter

with open("input.txt") as file:
  lines = file.readlines()

lines = [x.strip() for x in lines]

# Assuming every binary input is of equal length
binary_len = len(lines[0])

def get_rating(commonality):
  filtered_binaries = lines
  i = 0
  
  while i < binary_len:
    bits_at_index = list(map(lambda binary: binary[i], filtered_binaries))
    most_common_data = Counter(bits_at_index).most_common()
    most_common_bit = most_common_data[0][0] if commonality == "most" else most_common_data[1][0]

    if most_common_data[0][1] == most_common_data[1][1]:
      most_common_bit = "1" if commonality == "most" else "0"

    filtered_binaries = list(filter(lambda binary: binary[i] == most_common_bit, filtered_binaries))

    i += 1
    if (len(filtered_binaries) == 1):
      break

  return list(filtered_binaries)[0]

oxygen_generator_rating_binary = get_rating("most")
oxygen_generator_rating_decimal = int(oxygen_generator_rating_binary, 2)
print("oxygen generator rating binary", oxygen_generator_rating_binary)
print("oxygen generator rating decimal", oxygen_generator_rating_decimal)

CO2_scrubber_rating_binary = get_rating("least")
CO2_scrubber_rating_decimal =  int(CO2_scrubber_rating_binary, 2)
print("CO2 scrubber rating", CO2_scrubber_rating_binary)
print("CO2 scrubber rating", CO2_scrubber_rating_decimal)

print("life support rating", oxygen_generator_rating_decimal * CO2_scrubber_rating_decimal)
