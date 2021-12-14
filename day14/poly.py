from __future__ import annotations

from collections import defaultdict
from typing import Any, TypeVar

Element = str
Polymer = list[Element]
Pair = tuple[Element, Element]
PairInsertions = dict[Pair, Element]


def str_to_pair_insertion(t_str) -> tuple[Pair, Element]:
    split = t_str.split(" -> ")
    return (split[0][0], split[0][1]), split[1]


def parse_input(text: str) -> tuple[Polymer, PairInsertions]:
    split = text.split("\n\n")
    polymer = list(split[0])

    pair_insertions: PairInsertions = {}
    for line in split[1].splitlines():
        pair, element = str_to_pair_insertion(line)
        pair_insertions[pair] = element

    return polymer, pair_insertions


def get_split_pairs(
    pair_insertions: PairInsertions,
) -> dict[Pair, tuple[tuple[Pair, Pair], Element]]:
    pair_splits = {}
    for pair, insertion in pair_insertions.items():
        pair_splits[pair] = ((pair[0], insertion), (insertion, pair[1])), insertion

    return pair_splits


T = TypeVar("T")


def max_dict_value(a_dict: dict[Any, T]) -> T:
    return max(a_dict.items(), key=lambda i: i[1])[1]


def min_dict_value(a_dict: dict[Any, T]) -> T:
    return min(a_dict.items(), key=lambda i: i[1])[1]


def super_sick_algo(
    template: Polymer, pair_insertions: PairInsertions, steps: int
) -> int:
    """
    Ok so this took me way too long to figure out. The key is realizing there is
    no reason to keep track of a list at all. In fact, solutions will time out or run out
    of mem because the array you are building is too long.

    instead, you just need to keep track of how many pairs you have, in any order.
    From any pair, you already know which 2 pairs it generates, as well as the new element that
    is added.

    Thus, after initializing your pairs/counts in the template, you can just go
    step by step, generating new sets of pairs for all of your current pairs, and incrementing
    your counts.

    The result is an algorithm that takes O(1) space and O(N*M) time,
    where N is number of steps and M is number of distinct elements.
    """
    pair_splits = get_split_pairs(pair_insertions)
    pair_counter = defaultdict(lambda: 0)
    total_counts = defaultdict(lambda: 0)

    # setup
    for e in template:
        total_counts[e] += 1

    for e1, e2 in zip(template[:-1], template[1:]):
        pair_counter[(e1, e2)] += 1

    # algo
    for step in range(steps):
        new_pair_counter = defaultdict(lambda: 0)

        for pair, count in pair_counter.items():
            (pair1, pair2), insertion = pair_splits[pair]
            new_pair_counter[pair1] += count
            new_pair_counter[pair2] += count
            total_counts[insertion] += count

        pair_counter = new_pair_counter

    return max_dict_value(total_counts) - min_dict_value(total_counts)


def main():
    with open("input.txt") as f:
        template, pair_insertions = parse_input(f.read())
    print("Part 1: ", super_sick_algo(template, pair_insertions, 10))
    print("Part 2: ", super_sick_algo(template, pair_insertions, 40))


if __name__ == "__main__":
    main()
