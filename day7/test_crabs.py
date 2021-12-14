from day7.crabs import part1


def fixture() -> list[int]:
    return [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def test_part1():
    assert part1(fixture()) == 37
