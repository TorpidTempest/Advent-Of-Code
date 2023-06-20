from utils.get_input import get_input


def part1():
    data = get_input(puzzle_number=1)
    count, previous = 0, int(data[0])
    for point in data:
        if (current := int(point)) > previous:
            count += 1
        previous = current

    return count


def part2():
    data = get_input(puzzle_number=1)
    int_data = [int(el) for el in data]
    count = 0
    previous = sum(int_data[:3])
    for i in range(len(int_data) - 2):
        current = sum(int_data[i : i + 3])
        count += 1 if current > previous else 0
        previous = current

    return count


def main():
    print("Puzzle 1")
    print(f"Part 1: {part1()}")

    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
