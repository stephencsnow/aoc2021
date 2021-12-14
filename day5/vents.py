from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    @classmethod
    def from_str(cls, str_point: str) -> Point:
        """Expects 3,4"""
        split = str_point.split(",")
        return Point(x=int(split[0]), y=int(split[1]))


Line = tuple[Point, Point]


def parse_input(text: str) -> list[Line]:
    points = []
    for line in text.splitlines():
        str_points = line.split(" -> ")
        points.append((Point.from_str(str_points[0]), Point.from_str(str_points[1])))

    return points


def filter_only_vertical_horizontal(points: Iterable[Line]) -> list[Line]:
    """Given a list of lines, return only those that are vertical
    or horizontal.
    """
    result = []
    for p1, p2 in points:
        if p1.x == p2.x or p1.y == p2.y:
            result.append((p1, p2))

    return result

def points_in_line(point1: Point, point2: Point) -> list[Point]:
    """Assumes horizontal or vertical line"""
    match point1, point2:
        case Point(x1, y1), Point(x2, y2) if x1 == x2:
            # horizontal
            return [Point(x1, y) for y in range(min(y1, y2), max(y2, y1) + 1)]
        case Point(x1, y1), Point(x2, y2) if y1 == y2:
            # vertical
            return [Point(x, y1) for x in range(min(x1, x2), max(x2, x1) + 1)]
        case _:
            raise AssertionError("Not horizontal or vertical")


def part1(points: Iterable[Line]) -> int:
    """
    The general algorithm I will use is storing each "seen" coordinate in a counter dict.
    Every time the counter increments from 1 to 2, increment the total.
    """
    points = filter_only_vertical_horizontal(points)

    intersections: dict[Point, int] = defaultdict(lambda: 0)

    for p1, p2 in points:
        for point in points_in_line(p1, p2):
            intersections[point] += 1

    # finally, get how many points are intersecting
    return len([p for p, count in intersections.items() if count > 1])


def main():
    with open("input.txt") as f:
        data = parse_input(f.read())
    print(part1(data))


if __name__ == "__main__":
    main()