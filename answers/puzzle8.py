# %%
from get_input import get_input

Strings = list[str]


def main() -> None:
    print(f"Part 1: {part1()}\nPart 2: {part2()}")


def decode_display(inputs: Strings, outputs: Strings) -> int:
    decoded = {
        0: {""},
        1: {""},
        2: {""},
        3: {""},
        4: {""},
        5: {""},
        6: {""},
        7: {""},
        8: {""},
        9: {""},
    }
    fives, sixes = [], []
    for digit in inputs:
        match len(digit):
            case 2:
                decoded[1] = set(digit)
            case 3:
                decoded[7] = set(digit)
            case 4:
                decoded[4] = set(digit)
            case 5:
                fives.append(digit)
            case 6:
                sixes.append(digit)
            case 7:
                decoded[8] = set(digit)
            case _:
                print("error has occurred")

    for six in sixes:
        set6 = set(six)
        if not decoded[1].issubset(set6):
            decoded[6] = set6
        elif not decoded[4].issubset(set6):
            decoded[0] = set6
        else:
            decoded[9] = set6

    for five in fives:
        set5 = set(five)
        if decoded[1].issubset(set5):
            decoded[3] = set5
        elif set5.issubset(decoded[9]):
            decoded[5] = set5
        else:
            decoded[2] = set5

    output_strings = []
    for string in outputs:
        for num in decoded.keys():
            if set(string) == decoded[num]:
                output_strings.append(str(num))

    number = ""
    for string in output_strings:
        number += string

    return int(number)


# %%
def part1() -> int:
    raw = get_input(file_name="puzzle8.txt")
    output = []
    for line in raw:
        output_line = line.split("|")
        digits = output_line[1].strip().split(" ")
        for digit in digits:
            output.append(digit)
    count = 0
    for digit in output:
        length = len(digit)
        if length in [2, 3, 4, 7]:
            count += 1
    return count


# %%
def part2() -> int:
    raw2 = get_input(file_name="puzzle8.txt")
    output2 = []
    for line in raw2:
        output_line = line.split("|")
        inputs = output_line[0].strip().split(" ")
        outputs = output_line[1].strip().split(" ")
        output2.append([inputs, outputs])

    total = 0

    for num in output2:
        total += decode_display(num[0], num[1])

    return total


# %%
if __name__ == "__main__":
    main()
