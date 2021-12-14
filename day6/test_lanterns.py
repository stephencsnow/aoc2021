from day6.lanterns import cycle


def test_part1():
    assert cycle([3, 4, 3, 1, 2], 80) == 5934


def test_part2():
    assert cycle([3, 4, 3, 1, 2], 256) == 26984457539
