from .poly import parse_input, Polymer, PairInsertions, super_sick_algo


def fixture() -> tuple[Polymer, PairInsertions]:
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
    template, pair_insertions = fixture()
    assert super_sick_algo(template, pair_insertions, 10) == 1588


def test_part2():
    template, pair_insertions = fixture()
    assert super_sick_algo(template, pair_insertions, 40) == 2188189693529
