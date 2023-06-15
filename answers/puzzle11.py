from dataclasses import dataclass
from get_input import get_input
import itertools


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
        self.energy_level += 1
        return self.energy_level == 10

    def reset_if_flashed(self):
        if self.energy_level > 9:
            self.energy_level = 0
            self.flashes += 1

    def get_neighbours(self) -> set[Coordinate]:
        neighbours = set()
        x_choices = self.position.x + 1, self.position.x, self.position.x - 1
        y_choices = self.position.y - 1, self.position.y, self.position.y + 1
        valid_values = range(10)
        valid_positions = [
            coord
            for coord in itertools.product(x_choices, y_choices)
            if coord[0] in valid_values
            and coord[1] in valid_values
            and not (coord == (self.position.x, self.position.y))
        ]
        for pos in valid_positions:
            neighbours.add(Coordinate(*pos))

        return neighbours


def generate_octopus_field(puzzle_input: list[str]) -> dict[Coordinate, Octopus]:
    octopus_field: dict[Coordinate, Octopus] = {}
    for y, row in enumerate(puzzle_input):
        for x, energy in enumerate(row):
            pos = Coordinate(x, y)
            octopus_field.update({pos: Octopus(int(energy), pos)})
    return octopus_field



def update_energy(octopus_field: dict[Coordinate, Octopus], to_increment: set[Coordinate]):
    flashes: set[Coordinate] = set()
    for octopus in [octopus_field.get(coord) for coord in to_increment]:
        if octopus and octopus.increment():
            flashes.add(octopus.position)
            
    if not flashes:
        for octopus in octopus_field.values():
            octopus.reset_if_flashed()
        return
            
    flashed_by_neighbours: set[Coordinate] = set()
    for coord in flashes:
        if (octopus := octopus_field.get(coord)):
            flashed_by_neighbours.union(octopus.get_neighbours())
        
    update_energy(octopus_field, flashed_by_neighbours)
            
            


def puzzle1():
    puzzle_input = get_input("puzzle11.txt")
    octopus_field = generate_octopus_field(puzzle_input)

    for i in range(100):
        print(i)
        update_energy(octopus_field, set(octopus_field.keys()))
        
        
    total_flashes = 0
    for oct in octopus_field.values():
        total_flashes += oct.flashes
        
    print(total_flashes)
        



def main():
    puzzle1()


if __name__ == "__main__":
    main()
