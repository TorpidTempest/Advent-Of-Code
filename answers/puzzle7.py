# %% Run me 1st if using VSCode Interactive Window
from statistics import mean, median
from get_input import get_input

# %% Puzzle 1 Part 1
def part1() -> int:
    raw = get_input("puzzle7.txt")
    # * Funky flattened list comprehension, first time trying this
    numbers = [int(num) for line in raw for num in line.split(",")]

    # ? How to find the meeting point?
    meeting_point = median(numbers)

    fuel = 0
    for num in numbers:
        fuel += abs(num - meeting_point)
    return int(fuel)


# %%
def part2() -> int:
    raw2 = get_input("puzzle7.txt")
    # * Funky flattened list comprehension, first time trying this
    numbers2 = [int(num) for line in raw2 for num in line.split(",")]

    # ? Presumably the new meeting point is now the mean instead of median
    meeting_point2 = int(mean(numbers2))

    fuel2 = 0
    for num in numbers2:
        distance2 = abs(num - meeting_point2)
        fuel2 += sum(range(distance2 + 1))
        return fuel2


# %%
def main() -> None:
    print(f"Part 1: {part1()}\nPart 2: {part2()}")


if __name__ == "__main__":
    main()

# %%
