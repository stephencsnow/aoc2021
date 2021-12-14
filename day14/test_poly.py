from .poly import parse_input, Polymer, PairInsertion, part1


def fixture() -> tuple[Polymer, list[PairInsertion]]:
    text = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

    return parse_input(text)


def test_part1():
    data = fixture()
    assert part1(data[0], data[1]) == 1588
