from dataclasses import dataclass
from get_input import get_input


@dataclass(slots=True, frozen=True)
class Coordinate:
    x: int
    y: int
    
    
@dataclass(slots=True)
class Octopus:
    energy_level: int
    position: Coordinate
    flashes: int = 0
    
    def increment(self) -> bool:
        if self.energy_level > 9:
            return False
        self.energy_level += 1
        return self.energy_level > 9
    
    def end_step(self):
        if self.energy_level > 9:
            self.energy_level = 0
            self.flashes += 1
        
    
        
    


def puzzle1():
    puzzle_input = get_input("puzzle11.txt")
    octopus_field: dict[Coordinate, Octopus] = {}
    for y, row in enumerate(puzzle_input):
        for x, energy in enumerate(row):
            pos = Coordinate(x,y)
            octopus_field.update({pos:Octopus(int(energy), pos)})
            
    for _ in range(100):
        flashes: set[Coordinate] = set()
        for octopus in octopus_field.values():
            if flash := octopus.increment():
                flashes.add(octopus.position)
                



def main():
    puzzle1()
        
        
if __name__ == "__main__":
    main()