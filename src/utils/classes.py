from dataclasses import dataclass


@dataclass(slots=True)
class Coordinate:
    x: int
    y: int
    
    def __eq__(self, __value: 'Coordinate') -> bool:
        return self.x == __value.x and self.y == __value.y
    
    def __hash__(self) -> int:
        return hash(repr(self))