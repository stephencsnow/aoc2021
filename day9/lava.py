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


def main():
    with open("input.txt") as f:
        data = parse_data(f.read())
    print("Part 1: ", part1(data))


if __name__ == "__main__":
    main()
