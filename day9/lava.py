import math
from collections import Counter
from typing import Final

Coordinate = []

MAX_HEIGHT: Final[int] = 9

def parse_data(text: str) -> list[list[int]]:
    # first, convert to array of ints
    array = []
    for row in text.splitlines():
        array.append([int(point) for point in list(row)])

    return array


def get_neighbor_coordinates(i, j, n_rows, n_cols) -> list[tuple[int, int]]:
    """Given a point in an array, get the coordinates of the neighbors

    Assumes that the array does not wrap around.
    """
    coordinates = []
    if i > 0:
        coordinates.append((i - 1, j))
    if i < n_rows - 1:
        coordinates.append((i + 1, j))
    if j > 0:
        coordinates.append((i, j - 1))
    if j < n_cols - 1:
        coordinates.append((i, j + 1))
    return coordinates


def part1(array: list[list[int]]) -> int:
    risk_level = 0

    for i, row in enumerate(array):
        for j, height in enumerate(row):
            for i2, j2 in get_neighbor_coordinates(i, j, len(array), len(row)):
                if array[i2][j2] <= height:
                    # not a low point
                    break
            else:
                risk_level += 1 + height

    return risk_level


class QuickUnion:
    id: list[int]
    sz: list[int]

    def __init__(self, num_elements: int):
        self.id = list(range(num_elements))
        self.sz = list(1 for _ in range(num_elements))

    def _root(self, i: int) -> int:
        while i != self.id[i]:
            i = self.id[i]
        return i

    def as_rooted(self) -> list[int]:
        return [self._root(i) for i in self.id]

    def find(self, p: int, q: int) -> bool:
        return self._root(p) == self._root(q)

    def union(self, p: int, q: int) -> None:
        i = self._root(p)
        j = self._root(q)
        self.id[i] = j


def part2(array: list[list[int]]) -> int:
    """Union find, baby!

    https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf
    """
    m = len(array)
    n = len(array[0])
    quick_union = QuickUnion(m * n)

    for i, row in enumerate(array):
        for j, height in enumerate(row):
            if height == MAX_HEIGHT:
                continue

            for i2, j2 in get_neighbor_coordinates(i, j, len(array), len(row)):
                if array[i2][j2] != MAX_HEIGHT:
                    p = i * n + j
                    q = i2 * n + j2
                    quick_union.union(p, q)

    return math.prod(sorted(Counter(quick_union.as_rooted()).values(), reverse=True)[:3])



def main():
    with open("input.txt") as f:
        data = parse_data(f.read())
    print("Part 1: ", part1(data))
    print("Part 2: ", part2(data))


if __name__ == "__main__":
    main()
