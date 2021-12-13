with open("input.txt") as file:
  lines = file.readlines()

lines = [x.strip() for x in lines]

# List with a list for every bit in the input data
lists_of_bits_by_index = list(map(lambda bit: [], lines[0]))

for line in lines:
  for index, bit in enumerate(line):
    lists_of_bits_by_index[index].append(bit)

def most_frequent(list_of_bits):
  return max(set(list_of_bits), key = list_of_bits.count)

def get_inverse(binary):
  return "".join(list(map(lambda bit: "0" if bit == "1" else "1", binary)))

rate_gamma = "".join(list(map(lambda bit_list: most_frequent(bit_list), lists_of_bits_by_index)))
rate_epsilon = get_inverse(rate_gamma)

print("Gamma rate", rate_gamma)
print("Epsilon rate", rate_epsilon)

rate_gamma_decimal = int(rate_gamma, 2)
rate_epsilon_decimal = int(rate_epsilon, 2)

print("Power consumption", rate_gamma_decimal * rate_epsilon_decimal)