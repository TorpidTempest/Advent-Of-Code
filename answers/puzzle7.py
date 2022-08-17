# %% Run me 1st if using VSCode Interactive Window
from get_input import get_input

# %% Puzzle 1 Part 1
raw = get_input("../input_data/puzzle7.txt")
# * Funky flattened list comprehension, first time trying this
numbers = [int(num) for line in raw for num in line.split(",")]

meeting_point = 0 # ? How to find the meeting point?

fuel = 0
for num in numbers:
    fuel += abs(num-meeting_point)


# %%
