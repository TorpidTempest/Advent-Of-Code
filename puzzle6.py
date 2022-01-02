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
    new_fish = 0
    for i in range(len(a_list)):
        if a_list[i] == 0:
            a_list[i] = (cycle_length - 1)
            new_fish += 1
        else:
            a_list[i] -= 1
    for _ in range(new_fish):
        a_list.append(cycle_length + maturity_lag - 1)
    return a_list


def puzzle1(a_list):
    days = 80
    cycle_length = 7
    maturity_lag = 2
    for i in range(1, days + 1):
        a_list = a_day_passes(a_list, cycle_length, maturity_lag)
    print(f'There are {len(a_list)} lanternfish after {days} days')
            
def puzzle2(a_list):
    days = 256
    cycle_length = 7
    maturity_lag = 2
    for i in range(1, 10 + 1):
        a_list = a_day_passes(a_list, cycle_length, maturity_lag)
    fishDict = {}
    for fish in a_list:
        if fish not in fishDict:
            fishDict[fish] = 0
        fishDict[fish] += 1
    days_left = days - 10
    for _ in range(days_left):
        zeros = fishDict[0]
        for day in range(8):
            fishDict[day] = fishDict[day + 1]
        fishDict[8] = zeros
        fishDict[6] += zeros
    fish_sum = 0
    for day in fishDict:
        fish_sum += fishDict[day]
    print(f'After {days} days there are {fish_sum} fish')

# %%
