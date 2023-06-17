from dataclasses import dataclass, field
from get_input import get_input


@dataclass(slots=True)
class SmallCave:
    name: str
    neighbours: list[str] = field(default_factory=list)
    visited: bool = False
    
@dataclass(slots=True)
class BigCave:
    name: str
    neighbours: list[str] = field(default_factory=list)

def part1():
    puzzle_input = get_input(puzzle_number=12)
    
    
    
def main():
    part1()


if __name__ == "__main__":
    main()
