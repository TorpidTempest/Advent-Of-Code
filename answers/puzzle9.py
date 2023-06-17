from dataclasses import dataclass
from enum import Enum
from get_input import get_input


class IsLowest(Enum):
    """Is lowest options"""

    NO = 1
    MAYBE = 2
    YES = 3


class Neighbour(Enum):
    """Neighbour options"""

    LEFT = 1
    RIGHT = 2
    TOP = 3
    BOTTOM = 4


@dataclass
class Coordinate:
    """Coordinates"""

    x: int
    y: int

    def __repr__(self) -> str:
        return f"""({self.x}, {self.y})"""

    def __hash__(self) -> int:
        return hash((self.x, self.y))


@dataclass
class FloorPoint:
    """Floor point metadata"""

    coordinates: Coordinate
    height: int
    is_lowest: IsLowest
    basin: Coordinate | None = None
    checked: bool = False

    def set_basin(self, basin: Coordinate):
        self.basin = basin

    def set_checked(self):
        self.checked = True


def get_floor_height(path: str) -> list[list[int]]:
    """Get the floor heights from input data file"""

    lines = get_input(file_name=path)
    floor = []
    for line in lines:
        floor.append([int(x) for x in line])
    return floor


def get_floor_dict(floor: list[list[int]]) -> dict[Coordinate, FloorPoint]:
    """Generate a dictionary of all the points in the floor"""

    out = dict[Coordinate, FloorPoint]()
    for y, row in enumerate(floor):
        for x, height in enumerate(row):
            coord = Coordinate(x, y)
            point = FloorPoint(coord, height, IsLowest.MAYBE)
            out.update({(coord): point})

    return out


def is_lowest_point(
    floor: list[list[int]], rows: int, cols: int, coord: Coordinate
) -> bool:
    """Determines whether a point is a local lowest point"""

    right = left = top = bottom = False
    if coord.x == 0:
        right = check_neighour(coord, floor, Neighbour.RIGHT)
        left = True
    elif coord.x == cols - 1:
        left = check_neighour(coord, floor, Neighbour.LEFT)
        right = True
    else:
        left = check_neighour(coord, floor, Neighbour.LEFT)
        right = check_neighour(coord, floor, Neighbour.RIGHT)

    if coord.y == 0:
        top = True
        bottom = check_neighour(coord, floor, Neighbour.BOTTOM)
    elif coord.y == rows - 1:
        top = check_neighour(coord, floor, Neighbour.TOP)
        bottom = True
    else:
        top = check_neighour(coord, floor, Neighbour.TOP)
        bottom = check_neighour(coord, floor, Neighbour.BOTTOM)

    return left and right and top and bottom


def check_neighour(coord: Coordinate, floor, direction: Neighbour) -> bool:
    """Checks a point compared to one neightbour"""
    match direction:
        case Neighbour.LEFT:
            return compare_points(coord.x, coord.y, coord.x - 1, coord.y, floor)
        case Neighbour.BOTTOM:
            return compare_points(coord.x, coord.y, coord.x, coord.y + 1, floor)
        case Neighbour.TOP:
            return compare_points(coord.x, coord.y, coord.x, coord.y - 1, floor)
        case Neighbour.RIGHT:
            return compare_points(coord.x, coord.y, coord.x + 1, coord.y, floor)


def compare_points(x1: int, y1: int, x2: int, y2: int, floor: list[list[int]]) -> bool:
    """Checks if point 1 is lower than point 2"""
    return floor[y1][x1] < floor[y2][x2]


# %%
def get_lowest_values(filepath: str) -> list[int]:
    """Get the depths of the local lowest points"""
    lowest_values = []
    # get floor heights from file
    floor = get_floor_height(filepath)
    rows = len(floor)
    cols = len(floor[0])
    # add metadata to coordinates
    floor_dict = get_floor_dict(floor)
    # iterate through coordinates to determine their status as low points
    for coordinates, point in floor_dict.items():
        if is_lowest_point(floor, rows, cols, coordinates):
            point.is_lowest = IsLowest.YES
            lowest_values.append(point.height)
        else:
            point.is_lowest = IsLowest.NO

    # return low_points
    return lowest_values


def get_lowest_points(filepath: str) -> list[FloorPoint]:
    """Get the coordinates of the local lowest points"""
    lowest_points = []
    floor = get_floor_height(filepath)
    rows = len(floor)
    cols = len(floor[0])
    floor_dict = get_floor_dict(floor)

    for coordinates, point in floor_dict.items():
        if is_lowest_point(floor, rows, cols, coordinates):
            point.is_lowest = IsLowest.YES
            point.basin = point.coordinates
            lowest_points.append(point)
        else:
            point.is_lowest = IsLowest.NO

    return lowest_points


def build_basins(
    floor: dict[Coordinate, FloorPoint], low_points: list[FloorPoint]
) -> dict[Coordinate, set[FloorPoint]]:
    """Build up the basins from their lowest points until they merge with another
    basin or hit a boundary (a point of height 9)"""
    basins = dict[Coordinate, set[FloorPoint]]()
    for coord, point in floor.items():
        if point.height == 9:
            point.basin = coord
            basins.update({coord: set([point])})
        if point in low_points:
            point.basin = coord
            basins.update({coord: set([point])})
    print(low_points)

    return basins


def puzzle1() -> tuple[list[int], int]:
    """Solve puzzle 1"""
    input_data = "puzzle9.txt"
    lowest_values = get_lowest_values(input_data)
    risk_factor = len(lowest_values)
    for point in lowest_values:
        risk_factor += point

    return (lowest_values, risk_factor)


def puzzle2():
    """Solve puzzle 2"""
    input_data = "puzzle9-test.txt"
    basins = build_basins(
        get_floor_dict(get_floor_height(input_data)), get_lowest_points(input_data)
    )
    print(basins.keys())


def main():
    """Run both puzzles"""
    lowest_values, risk_factor = puzzle1()
    print(
        f"PUZZLE 1\nLowest points are : {lowest_values} \n"
        + f"Risk factor: {risk_factor}\nNo of points: {len(lowest_values)}"
    )
    print("\n")
    puzzle2()


if __name__ == "__main__":
    main()
