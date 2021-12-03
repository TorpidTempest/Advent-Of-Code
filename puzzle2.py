# %% Run me 1st if using VSCode Interactive Window
from get_input import get_input

# %% Puzzle 2 Part 1
input_list = get_input("input_data/puzzle2.txt")

distance = 0
depth = 0

for command in input_list:
    if 'forward' in command:
        distance += int(''.join(filter(str.isdigit, command)))
    if 'down' in command:
        depth += int(''.join(filter(str.isdigit, command)))
    if 'up' in command:
        depth -= int(''.join(filter(str.isdigit, command)))

print(distance)
print(depth)
print(distance*depth)

# %% Puzzle 2 Part 2
input_list = get_input("input_data/puzzle2.txt")

distance = 0
depth = 0
aim = 0

# I'm sure there is a more elegant way to pull ints from string but it works
for command in input_list:
    if 'forward' in command:
        magnitude = int(''.join(filter(str.isdigit, command)))
        distance += magnitude
        depth += magnitude * aim
    if 'down' in command:
        aim += int(''.join(filter(str.isdigit, command)))
    if 'up' in command:
        aim -= int(''.join(filter(str.isdigit, command)))

print(distance)
print(depth)
print(distance*depth)


# %%
