from functools import cache
import itertools
from utils.get_input import get_input

@cache
def grow_polymer(template: str, steps: int) -> str:
    to_insert: list[str] = []
    for pair in itertools.pairwise(template):
        to_insert.append(rules.get("".join(pair), ""))

    zipped = itertools.zip_longest(template, to_insert, fillvalue="")
    flattened = (''.join(pair) for pair in zipped)
    return "".join(flattened)


def run(steps: int):
    puzzle_input = get_input(puzzle_number=14)
    template = puzzle_input[0]
    global rules
    rules = {line[:2]: line[-1] for line in puzzle_input[1:] if line}

    for i in range(steps):
        print(i)
        print(len(template))
        template = grow_polymer(template)

    res: dict[str,int] = {}
    for char in template:
        if res.get(char):
            res[char] += 1
        else:
            res.update({char:1})
            
    most = max(res.values())
    least = min(res.values())
    
    
    common = ''.join(f"{k}: {v}" for k,v in res.items() if v == most)
    rare = ''.join(f"{k}: {v}" for k,v in res.items() if v == least)
    
    print(common)
    print(rare)
    print(most - least)
   
   
   
def part1():
    run(10)
    
    
def part2():
    print('\U0001F4A9'*1000)
    run(40)


def main():
    print("\n\033[1;32mPart 1\033[0m\n")
    part1()
    
    print("\n\033[1;32mPart 2\033[0m\n")
    part2()


if __name__ == "__main__":
    main()
