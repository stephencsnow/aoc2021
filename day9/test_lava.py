from day9.lava import parse_data, part1


def fixture() -> list[list[int]]:
    text = """2199943210
3987894921
9856789892
8767896789
9899965678"""

    return parse_data(text)


def test_part1():
    assert part1(fixture()) == 15
