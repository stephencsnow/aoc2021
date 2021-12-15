from __future__ import annotations

from collections import Counter
from dataclasses import dataclass

Signal = str
SignalPattern = set[Signal]
OutputValue = list[SignalPattern]


DIGIT_TO_SEGMENT = {
    0: set("abcefg"),
    1: set("cf"),
    2: set("acdeg"),
    3: set("acdfg"),
    4: set("bcdf"),
    5: set("abdfg"),
    6: set("abdefg"),
    7: set("acf"),
    8: set("abcdefg"),
    9: set("abcdfg"),
}


@dataclass
class Entry:
    signal_patterns: list[SignalPattern]
    output_value: OutputValue

    @classmethod
    def from_string(cls, text: str) -> Entry:
        signal_patterns, output_value = text.split(" | ")
        return cls(
            signal_patterns=[set(pattern) for pattern in signal_patterns.split()],
            output_value=[set(pattern) for pattern in output_value.split()]
        )


def parse_data(text: str) -> list[Entry]:
    entries = []
    for line in text.splitlines():
        entries.append(Entry.from_string(line))

    return entries


def get_unique_segment_lengths() -> set[int]:
    length_counter = Counter([len(x) for x in DIGIT_TO_SEGMENT.values()])
    return {length for length, count in length_counter.items() if count == 1}


def part1(entries: list[Entry]) -> int:
    """Count number of output digits that contain "unique" number of segments"""
    unique_segment_lengths = get_unique_segment_lengths()

    count = 0
    for entry in entries:
        count += len([digit for digit in entry.output_value if len(digit) in unique_segment_lengths])

    return count


def main():
    with open("input.txt") as f:
        entries = parse_data(f.read())
    print("Part 1", part1(entries))


if __name__ == "__main__":
    main()
