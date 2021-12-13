# %%
from get_input import get_input
import re

raw_input = get_input("input_data/puzzle5.txt")
for line in raw_input:
    line.replace('->', ',')
    raw_input[line] = line.split(',')
# %%
