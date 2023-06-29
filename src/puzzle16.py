from dataclasses import dataclass
from typing import Literal
from utils.get_input import get_input

GREEN = "\033[1;32m"
RESET = "\033[0m"

class Packet:
    version: int
    type_id: int
    length_type: int
    subpackets: list['Packet'] # todo make generic packet content
    literal_value: int | None
    
    def __init__(self, binary_num: str) -> None:
        length = len(binary_num)
        self.version = int(binary_num[0:3], 2)
        self.type_id = int(binary_num[3:6], 2)
        self.length_type = int(binary_num[6])
        # todo finish init()
        
        
        

def hex_to_bin(hex_num: str) -> str:
    return bin(int(hex_num, 16))


def bin_to_hex(bin_num: str | bytes | bytearray) -> str:
    return hex(int(bin_num, 2))


def parse_for_packets(bin_num: str) -> tuple[str, int]:
    if int(bin_num, 2) == 0:
        return "0", 0

    packet_version = int("".join(bin_num[0:3]), 2)
    type_id = int("".join(bin_num[3:6]), 2)

    literal_value = True if type_id == 4 else False
    if literal_value:
        return "0", 0 # not relevant for part1
    else:
        length_id = bin_num[6]
        if length_id:
            num_packets = int(bin_num[7:7+11])
        else:
            packets_length = int(bin_num[7:7+15])
        
        

    print(packet_version, type_id)

    return bin_num, packet_version


def part1():
    puzzle_input = get_input(puzzle_number=16)[0]
    binary_input = hex_to_bin(puzzle_input)[2:]

    versions = []
    while binary_input != "0":
        binary_input, version = parse_for_packets(binary_input)
        versions.append(version)

    print(versions)


def part2():
    puzzle_input = get_input(puzzle_number=16)


def main():
    print(f"\n{GREEN}Part 1{RESET}:\n{part1()}")

    print(f"{GREEN}Part 2{RESET}:\n{part2()}\n")


if __name__ == "__main__":
    main()
