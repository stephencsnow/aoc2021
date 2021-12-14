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


def inclusive_range(start: int, end: int) -> range:
    if end >= start:
        return range(start, end + 1)
    else:
        return range(start, end - 1, -1)


def points_in_line(point1: Point, point2: Point) -> list[Point]:
    """Assumes horizontal, diagonal, or vertical line"""
    match point1, point2:
        case Point(x1, y1), Point(x2, y2) if x1 == x2:
            # vertical
            return [Point(x1, y) for y in inclusive_range(y1, y2)]
        case Point(x1, y1), Point(x2, y2) if y1 == y2:
            # horizontal
            return [Point(x, y1) for x in inclusive_range(x1, x2)]
        case Point(x1, y1), Point(x2, y2) if abs(x2 - x1) == abs(y2 - y1):
            # diagonal
            return [
                Point(x, y)
                for x, y in zip(inclusive_range(x1, x2), inclusive_range(y1, y2))
            ]
        case _:
            raise AssertionError("Line must be horizontal, vertical, or diagonal")


def num_intersecting_points(intersection_counter: dict[Point, int]) -> int:
    return len([p for p, count in intersection_counter.items() if count > 1])


def part1(points: Iterable[Line]) -> int:
    """
    The general algorithm I will use is storing each "seen" coordinate in a counter dict.
    Every time the counter increments from 1 to 2, increment the total.
    """
    points = filter_only_vertical_horizontal(points)

    intersection_counter: dict[Point, int] = defaultdict(lambda: 0)

    for p1, p2 in points:
        for point in points_in_line(p1, p2):
            intersection_counter[point] += 1

    # finally, get how many points are intersecting
    return num_intersecting_points(intersection_counter)


def part2(points: Iterable[Line]) -> int:
    """
    Same as part2, but don't filter lines
    """
    intersection_counter: dict[Point, int] = defaultdict(lambda: 0)

    for p1, p2 in points:
        for point in points_in_line(p1, p2):
            intersection_counter[point] += 1

    # finally, get how many points are intersecting
    return num_intersecting_points(intersection_counter)


def main():
    with open("input.txt") as f:
        data = parse_input(f.read())
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
