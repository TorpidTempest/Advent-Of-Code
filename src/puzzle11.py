from dataclasses import dataclass
from utils.get_input import get_input
from utils.classes import Coordinate
import itertools



@dataclass(slots=True)
class Octopus:
    energy_level: int
    position: Coordinate
    flashes: int = 0
    flashed: bool = False

    def increment(self):
        self.energy_level += 1
        if self.energy_level == 10:
            self.flashed = True

    def reset_if_flashed(self):
        if self.energy_level < 10:
            return False
        self.energy_level = 0
        self.flashes += 1
        return True

    def get_neighbours(self) -> list[Coordinate]:
        neighbours = []
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
            neighbours.append(Coordinate(*pos))

        return neighbours


def generate_octopus_field(puzzle_input: list[str]) -> dict[Coordinate, Octopus]:
    octopus_field: dict[Coordinate, Octopus] = {}
    for y, row in enumerate(puzzle_input):
        for x, energy in enumerate(row):
            pos = Coordinate(x, y)
            octopus_field.update({pos: Octopus(int(energy), pos)})
    return octopus_field


def update_energy(
    octopus_field: dict[Coordinate, Octopus], to_increment: list[Coordinate]
):
    flashes: list[Coordinate] = []  # ? Increment all octopii to_increment
    for coord in to_increment:
        (octopus := octopus_field[coord]).increment()
        if octopus.flashed:
            octopus.flashed = False
            flashes.append(octopus.position)

    if not flashes:
        return

    neighbours_flashed: list[Coordinate] = list()
    for coord in flashes:
        if octopus := octopus_field.get(coord):
            neighbours_flashed += octopus.get_neighbours()

    update_energy(octopus_field, neighbours_flashed)


def puzzle1():
    puzzle_input = get_input(file_name="puzzle11.txt")
    octopus_field = generate_octopus_field(puzzle_input)

    for i in range(100):
        update_energy(octopus_field, list(octopus_field.keys()))
        for octopus in octopus_field.values():
            octopus.reset_if_flashed()

    total_flashes = 0
    for oct in octopus_field.values():
        total_flashes += oct.flashes

    print(total_flashes)


def puzzle2():
    puzzle_input = get_input(file_name="puzzle11.txt")
    octopus_field = generate_octopus_field(puzzle_input)
    i = 0
    while True:
        i += 1
        update_energy(octopus_field, list(octopus_field.keys()))
        flashed = 0
        for octopus in octopus_field.values():
            flash = octopus.reset_if_flashed()
            if flash:
                flashed += 1
        if flashed == 100:

            print(i)
            return i


def main():
    puzzle1()
    puzzle2()


if __name__ == "__main__":
    main()
