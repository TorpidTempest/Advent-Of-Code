# %% Run me 1st if using VSCode Interactive Window
from get_input import get_input

# %% Puzzle 3 Part 1

input_list = get_input('puzzle3.txt')

"""
The most commonly occur bit in each position gives the gamma rate,
the least common gives the epsilon rate. The solution requires these 2 
numbers be multiplied together and expressed in decimal
"""

# Create an empty list to store the count of each of the bits
digits = len(input_list[0])
bit_count = []
for _ in range(digits):
    bit_count.append(0)

# Iterate over bits of each number in input list to count which is more common
for input_number in input_list:
    for i in range(digits):
        bit = input_number[i]
        if bit == '1':
            bit_count[i] +=1
        else:
            bit_count[i] -=1

print(bit_count)

# Find gamma

# Create a new list where each element is the most common bit in that position
number_list = []
for number in bit_count:
    if number > 0:
        number_list.append(1)
    else:
        number_list.append(0)

print(number_list)

num_str = ''

for element in number_list:
    num_str += str(element)

print(num_str)

gamma = int(num_str, 2)

print(f"Gamma - {gamma}")

# Generate Epsilon (by mirroring above example)

number_list_2 = []

for number in bit_count:
    if number > 0:
        number_list_2.append(0)
    else:
        number_list_2.append(1)

print(number_list_2)

num_str_2 = ''

for element in number_list_2:
    num_str_2 += str(element)

print(num_str_2)

epsilon = int(num_str_2, 2)

print(f"Epsilon - {epsilon}")

print(f"Gamma * Epsilon - {gamma * epsilon}")
# %% Puzzle 3 Part 2

input_list = get_input('puzzle3.txt')

# Create an empty list to store the count of each of the bits
digits = len(input_list[0])
bit_count = []
for _ in range(digits):
    bit_count.append(0)

# Iterate over bits of each number in input list to count which is more common
for input_number in input_list:
    for i in range(digits):
        bit = input_number[i]
        if bit == '1':
            bit_count[i] +=1
        else:
            bit_count[i] -=1

# Create a new list where each element is the most common bit in that position
number_list = []
for number in bit_count:
    if number > 0:
        number_list.append(1)
    else:
        number_list.append(0)

# Create a copy of the input list to be reduced at each digit
reducing_list = []
for element in input_list:
    reducing_list.append(element)

# Iterate through list removing numbers who have the least common digit in each place
for digit in range(digits):
    bit_count = 0
    for input_number in reducing_list:
        if input_number[digit] == '1':
            bit_count += 1
        else:
            bit_count -= 1
    bit = None
    if bit_count >= 0:
        bit = '1'
    else:
        bit = '0'
    for input_number in reducing_list[:]:
        if input_number[digit] != bit:
            reducing_list.remove(input_number)
    print(len(reducing_list))

    if len(reducing_list) == 1:
        break

print(reducing_list)
oxygen = int(reducing_list[0], 2)
print(f"Oxygen Generator Rating - {oxygen}")

# Create a copy of the input list to be reduced at each digit
reducing_list_2 = []
for element in input_list:
    reducing_list_2.append(element)

# Iterate through list removing numbers who have the least common digit in each place
for digit in range(digits):
    bit_count = 0
    for input_number in reducing_list_2:
        if input_number[digit] == '1':
            bit_count += 1
        else:
            bit_count -= 1
    bit = None
    if bit_count >= 0:
        bit = '0'
    else:
        bit = '1'
    for input_number in reducing_list_2[:]:
        if input_number[digit] != bit:
            reducing_list_2.remove(input_number)
    print(len(reducing_list_2))
    if len(reducing_list_2) == 1:
        break

print(reducing_list_2)
co2 = int(reducing_list_2[0], 2)
print(f"CO2 Scrubber Rating - {co2}")

print(f"Life support rating - {oxygen * co2}")
