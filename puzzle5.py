# %%
from get_input import get_input
import re

raw_input = get_input("input_data/puzzle5.txt")
cleaned_input = []
for line in raw_input:
    cleaned_input.append(line.split(' -> '))

def check_is_valid(coords_set):
    line = False
    if coords_set[0][0] == coords_set[1][0]:
        line = 'x'
    elif coords_set[0][1] == coords_set[1][1]:
        line = 'y'
    
    return line

def add_line(coords_set):
    if check_is_valid(coords_set) == 'x':
        # now to save the line somehow
        print('x')
    if check_is_valid(coords_set) == 'y':
        # As above or maybe combined
        print('y')
# %%
