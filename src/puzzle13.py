from typing import Literal
from utils.get_input import get_input
from utils.classes import Coordinate


def transform(points: list[Coordinate], axis: str, val: int) -> list[Coordinate]:
    for point in points:
        if (current := getattr(point, axis)) > val:
            setattr(point, axis, 2 * val - current)
    return list(set(points))


def part1():
    paper_data = get_input(puzzle_number=13)
    instructions = [line.split()[-1] for line in get_input(puzzle_number="13-A")]

    points = [
        Coordinate(int(x), int(y))
        for x, y in [point.split(",") for point in paper_data]
    ]
    axis, val = instructions[0].split("=")
    points = transform(points, axis, int(val))
    print(len(points))


def part2():
    paper_data = get_input(puzzle_number=13)
    instructions = [line.split()[-1] for line in get_input(puzzle_number="13-A")]

    points = [
        Coordinate(int(x), int(y))
        for x, y in [point.split(",") for point in paper_data]
    ]
    for instruction in instructions:
        axis, val = instruction.split("=")
        points = transform(points, axis, int(val))

    grid: list[list[str]] = list()
    for y in range(max([point.y + 1 for point in points])):
        row: list[str] = list()
        for x in range(max([point.x + 1 for point in points])):
            row.append("\u2588" if Coordinate(x, y) in points else " ")
        grid.append(row)
    for line in grid:
        print("".join(line))



#   ██ ███  ████  ██  █  █  ██  █  █ ███
#    █ █  █    █ █  █ █  █ █  █ █  █ █  █
#    █ █  █   █  █    █  █ █  █ █  █ █  █
#    █ ███   █   █    █  █ ████ █  █ ███
# █  █ █    █    █  █ █  █ █  █ █  █ █ █
#  ██  █    ████  ██   ██  █  █  ██  █  █        



def main():
    part1()
    print("\n\n")
    part2()


if __name__ == "__main__":
    main()
