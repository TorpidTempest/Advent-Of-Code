# %%
from enum import Enum
from typing import Dict, TypedDict
from xml.dom.expatbuilder import FilterVisibilityController
from get_input import get_input


# %% Classes to be used in solving problem
class IsLowest(Enum):
    """Is lowest options

    Args:
        Enum (_type_): enum vals
    """

    NO = 1
    MAYBE = 2
    YES = 3


class Neighbour(Enum):
    """Neighbour options

    Args:
        Enum (_type_): enum vals
    """

    LEFT = 1
    RIGHT = 2
    TOP = 3
    BOTTOM = 4


class Coordinate:
    """Coordinates

    Returns:
        _type_: N/A
    """

    x: int
    y: int

    def __repr__(self) -> str:
        return f"""
    X: {self.x}, 
    Y: {self.y},
    """


class FloorPoint:
    """Floor point metadata

    Returns:
        _type_: _
    """

    coordinates: Coordinate
    height: int
    is_lowest: IsLowest

    def __repr__(self) -> str:
        return f"""
    X: {self.coordinates.x}, 
    Y: {self.coordinates.y},
    height: {self.height}
    is_lowest: {self.is_lowest}
    """


# %%
def get_floor_height(path: str) -> list[list[int]]:
    """Get the floor heights from input data file

    Args:
        path (str): pathname as a string

    Returns:
        list[list[int]]: a 2D list of floor heights
    """
    lines = get_input(path)
    floor = []
    for line in lines:
        floor.append([int(x) for x in line])
    return floor


# %%
def get_floor_dict(floor: list[list[int]]) -> dict:
    """Generate a dictionary of all th points in the floor

    Args:
        floor (list[list[int]]): 2D array of data to become dictionary

    Returns:
        dict: Completed dictionary of metadata
    """
    out = dict()
    for y, row in enumerate(floor):
        for x, height in enumerate(row):
            coord = Coordinate()
            coord.x = x
            coord.y = y
            point = FloorPoint()
            point.coordinates = coord
            point.height = height
            point.is_lowest = IsLowest.MAYBE
            out.update({(x, y): point})

    return out


# %%
def is_lowest_point(
    floor: list[list[int]], rows: int, cols: int, x_coordinate: int, y_coordinate: int
) -> bool:
    """Determines whether a point is a local lowest point

    Args:
        floor (list[list[int]]): floor array
        rows (int): number of rows
        cols (int): number of columns
        x_coordinate (int): x coordinate
        y_coordinate (int): y coordinate

    Returns:
        bool: result
    """

    right = left = top = bottom = False
    if x_coordinate == 0:
        right = check_neighour(x_coordinate, y_coordinate, floor, Neighbour.RIGHT)
        left = True
    elif x_coordinate == cols - 1:
        left = check_neighour(x_coordinate, y_coordinate, floor, Neighbour.LEFT)
        right = True
    else:
        left = check_neighour(x_coordinate, y_coordinate, floor, Neighbour.LEFT)
        right = check_neighour(x_coordinate, y_coordinate, floor, Neighbour.RIGHT)

    if y_coordinate == 0:
        top = True
        bottom = check_neighour(x_coordinate, y_coordinate, floor, Neighbour.BOTTOM)
    elif y_coordinate == rows - 1:
        top = check_neighour(x_coordinate, y_coordinate, floor, Neighbour.TOP)
        bottom = True
    else:
        top = check_neighour(x_coordinate, y_coordinate, floor, Neighbour.TOP)
        bottom = check_neighour(x_coordinate, y_coordinate, floor, Neighbour.BOTTOM)

    return left and right and top and bottom


def check_neighour(x: int, y: int, floor, direction: Neighbour) -> bool:
    """Checks a point compared to one neightbour

    Args:
        x (int): _description_
        y (int): _description_
        floor (_type_): _description_
        direction (Neighbour): _description_

    Returns:
        bool: _description_
    """
    match direction:
        case Neighbour.LEFT:
            return compare_points(x, y, x - 1, y, floor)
        case Neighbour.BOTTOM:
            return compare_points(x, y, x, y + 1, floor)
        case Neighbour.TOP:
            return compare_points(x, y, x, y - 1, floor)
        case Neighbour.RIGHT:
            return compare_points(x, y, x + 1, y, floor)


def compare_points(x1: int, y1: int, x2: int, y2: int, floor: list[list[int]]) -> bool:
    return floor[y1][x1] < floor[y2][x2]


# %%
def solve_puzzle1(filepath: str):
    lowest_points = []
    # get floor heights from file
    floor = get_floor_height(filepath)
    rows = len(floor)
    cols = len(floor[0])
    # add metadata to coordinates
    floor_dict = get_floor_dict(floor)
    # iterate through coordinates to determine their status as low points
    for coordinates, point in floor_dict.items():
        floor_dict.update()
        if is_lowest_point(floor, rows, cols, coordinates[0], coordinates[1]):
            point.is_lowest = IsLowest.YES
            lowest_points.append(point.height)
        else:
            point.is_lowest = IsLowest.NO

    # return low_points
    return lowest_points


def puzzle1():
    input_data = "puzzle9.txt"
    lowest_points = solve_puzzle1(input_data)
    risk_factor = len(lowest_points)
    for point in lowest_points:
        risk_factor += point
    print(
        f"PUZZLE 1\nLowest points are : {lowest_points} \nRisk factor: {risk_factor}\nNo of points: {len(lowest_points)}"
    )


def puzzle2():
    print("PUZZLE 2")


def main():
    puzzle1()
    print("\n")
    puzzle2()


if __name__ == "__main__":
    main()
