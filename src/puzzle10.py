from collections import deque
from utils.get_input import get_input
from pathlib import Path


CHAR_MAP = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def find_invalid(line: str) -> str | None:
    queue: deque[str] = deque()
    for char in line:
        if char in CHAR_MAP.keys():
            queue.append(CHAR_MAP[char])
        elif queue.pop() != char:
            return char
    return None


def find_incomplete(line: str) -> deque[str] | None:
    queue: deque[str] = deque()
    for char in line:
        if char in CHAR_MAP.keys():
            queue.append(CHAR_MAP[char])
        elif char != queue.pop():
            return None
    if len(queue) == 0:
        print("GOT HIM")
    return queue


def puzzle1(input: list[str]):
    CHAR_SCORES = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    score = 0
    for line in input:
        if res := find_invalid(line):
            score += CHAR_SCORES.get(res)  # type: ignore

    return score


def puzzle2(data_input: list[str]):
    CHAR_SCORES = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    scores: list[int] = []
    for line in data_input:
        if res := find_incomplete(line):
            score = 0
            while res:
                score *= 5
                score += CHAR_SCORES.get(res.pop(), 0)
            scores.append(score)
    scores.sort()
    
    return scores[len(scores) // 2]


def main():
    """Run both puzzles"""
    file = f"{Path(__file__).name.split('.')[0]}.txt"
    input = get_input(file_name=file)

    first = puzzle1(input)
    print(f"1st: {first}")
    print("\n\n")
    second = puzzle2(input)
    print(f"2nd: {second}")  # 1163597899 is too small  # 1132372595


if __name__ == "__main__":
    main()
