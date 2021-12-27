# %%
from get_input import get_input

raw_input = get_input("input_data/puzzle6.txt")
input_list = []
for line in raw_input:
    input_list = line.split(',')
int_list = []
for number in input_list:
    int_list.append(int(number))

def a_day_passes(a_list, cycle_length, maturity_lag):
    next_gen = 0
    output = []
    for fish in a_list:
        if fish == 0:
            output.append(cycle_length - 1)
            next_gen += 1
        else:
            output.append(fish - 1)
    for _ in range(next_gen):
        output.append(cycle_length + maturity_lag - -1)
    return output


def puzzle1(a_list):
    days = 80
    cycle_length = 7
    maturity_lag = 2
    for i in range(days + 1):
        a_list = a_day_passes(a_list, cycle_length, maturity_lag)
        print(f'There are {len(a_list)} lanternfish after {i} days')
            

# %%
