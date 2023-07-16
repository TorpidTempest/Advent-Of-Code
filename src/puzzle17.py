import math


GREEN = "\033[1;32m"
RESET = "\033[0m"
TARGET_X = range(60, 95)
TARGET_Y = range(-171, -135)


def part1():
    # x velocity must be large enough to acheive target range before it hits 0 limit
    # slowest allows longest time to arc to greatest high point. ideally hits 0 in range

    x_min, x_max = 0, 0
    i = 1
    while not (x_min and x_max):
        val = math.factorial(i)
        if not x_min and val > TARGET_X[0]:
            x_min = i
        if x_min and val > TARGET_X[-1]:
            x_max = i - 1

        i += 1

    return x_min, x_max


def part2():
    pass


def main():
    print(f"\n{GREEN}Part 1{RESET}:\n{part1()}")

    print(f"{GREEN}Part 2{RESET}:\n{part2()}\n")


if __name__ == "__main__":
    main()
