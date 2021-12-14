from __future__ import annotations

from collections import Counter
from dataclasses import dataclass

Element = str
Polymer = list[Element]


@dataclass
class PairInsertion:
    pair: tuple[Element, Element]
    element: Element

    @classmethod
    def from_str(cls, t_str: str) -> PairInsertion:
        split = t_str.split(" -> ")
        return cls(pair=(split[0][0], split[0][1]), element=split[1])


def parse_input(text: str) -> tuple[Polymer, list[PairInsertion]]:
    split = text.split("\n\n")
    polymer = list(split[0])

    pair_insertions = []
    for line in split[1].splitlines():
        pair_insertions.append(PairInsertion.from_str(line))

    return polymer, pair_insertions


def algo(template: Polymer, pair_insertions: list[PairInsertion], steps: int) -> int:
    """Algo:

    keep track of insertions,
    then for each insertion, regenerate the list,
    then repeat steps
    """
    for step in range(steps):
        print(f"{step=}, len={len(template)}")
        inserts: list[tuple[int, Element]] = []
        for idx in range(1, len(template)):
            first = template[idx - 1]
            second = template[idx]
            for pair_insertion in pair_insertions:
                if (first, second) == pair_insertion.pair:
                    # going to insert!
                    inserts.append((idx, pair_insertion.element))
        # ok done with determining inserts, now let us add them
        # first, let's sort the inserts so there is no funny business
        inserts.sort(key=lambda x: x[0])

        for num_inserted, (insert_idx, element) in enumerate(inserts):
            template.insert(insert_idx + num_inserted, element)

    counts: dict[str, int] = Counter(template)

    return max(counts.items(), key=lambda i: i[1])[1] - min(counts.items(), key=lambda i: i[1])[1]


def part1(template: Polymer, pair_insertions: list[PairInsertion]) -> int:
    return algo(template, pair_insertions, 10)


def part2(template: Polymer, pair_insertions: list[PairInsertion]) -> int:
    return algo(template, pair_insertions, 40)


def main():
    with open("input.txt") as f:
        template, pair_insertions = parse_input(f.read())
    print(part1(template, pair_insertions))
    #print(part2(template, pair_insertions))


if __name__ == "__main__":
    main()
