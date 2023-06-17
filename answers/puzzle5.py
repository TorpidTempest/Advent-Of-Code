# %%
from get_input import get_input
import numpy as np


def add_lines_1(coords_set, ocean_floor) -> None:
    x1, x2 = int(coords_set[0][0]), int(coords_set[1][0])
    y1, y2 = int(coords_set[0][1]), int(coords_set[1][1])
    ascending = 1
    if x1 == x2:
        x = x1
        if y1 > y2:
            ascending = -1
        for y in range(y1, y2 + ascending, ascending):
            ocean_floor[x][y] += 1

    elif y1 == y2:
        y = y1
        if x1 > x2:
            ascending = -1
        for x in range(x1, x2 + ascending, ascending):
            ocean_floor[x][y] += 1


def add_lines_2(coords_set, ocean_floor) -> None:
    x1, x2 = int(coords_set[0][0]), int(coords_set[1][0])
    y1, y2 = int(coords_set[0][1]), int(coords_set[1][1])
    ascending = 1
    if x1 == x2:
        x = x1
        if y1 > y2:
            ascending = -1
        for y in range(y1, y2 + ascending, ascending):
            ocean_floor[x][y] += 1

    elif y1 == y2:
        y = y1
        if x1 > x2:
            ascending = -1
        for x in range(x1, x2 + ascending, ascending):
            ocean_floor[x][y] += 1

    elif abs(y2 - y1) == abs(x2 - x1):
        steps = abs(x2 - x1) + 1
        x_iterator, y_iterator = 1, 1
        if x1 > x2:
            x_iterator = -1
        if y1 > y2:
            y_iterator = -1
        x, y = x1, y1
        for _ in range(steps):
            ocean_floor[x][y] += 1
            x += x_iterator
            y += y_iterator


def puzzle1() -> str:
    raw_input = get_input(file_name="puzzle5.txt")
    input_list = []
    for line in raw_input:
        line = line.split(" -> ")
        input_list.append(line)
    final_list = []
    for coords in input_list:
        final_coords = []
        for coord in coords:
            final_coords.append(coord.split(","))
        final_list.append(final_coords)

    ocean_floor = np.zeros((1000, 1000), dtype=np.int32)
    for coords in final_list:
        add_lines_1(coords, ocean_floor)

    danger_zones = 0
    for x in ocean_floor:
        for y in x:
            if y > 1:
                danger_zones += 1

    return f"The number of danger zones = {danger_zones}"


def puzzle2() -> str:
    raw_input = get_input(file_name="puzzle5.txt")
    input_list = []
    for line in raw_input:
        line = line.split(" -> ")
        input_list.append(line)
    final_list = []
    for coords in input_list:
        final_coords = []
        for coord in coords:
            final_coords.append(coord.split(","))
        final_list.append(final_coords)

    ocean_floor = np.zeros((1000, 1000), dtype=np.int32)
    for coords in final_list:
        add_lines_2(coords, ocean_floor)

    danger_zones = 0
    for x in ocean_floor:
        for y in x:
            if y > 1:
                danger_zones += 1

    return f"The number of danger zones = {danger_zones}"


# %%


def main() -> None:
    print(f"Part 1: {puzzle1()}\nPart 2: {puzzle2()}")


if __name__ == "__main__":
    main()
