from .vents import part1, parse_input, Point, filter_only_vertical_horizontal


def fixture() -> list[tuple[Point, Point]]:
    text = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""
    return parse_input(text)


def test_filter_only_vertical_horizontal():
    data = [
        (Point(1, 2), Point(1, 4)),
        (Point(2, 1), Point(4, 1)),
        (Point(2, 1), Point(4, 4)),
    ]
    assert filter_only_vertical_horizontal(data) == [
        (Point(1, 2), Point(1, 4)),
        (Point(2, 1), Point(4, 1))
    ]


def test_part1():
    points = fixture()
    assert part1(points) == 5
