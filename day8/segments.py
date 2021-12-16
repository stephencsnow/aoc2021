from __future__ import annotations

from dataclasses import dataclass

Segment = str
Wire = str
SignalPattern = set[Wire]
OutputValue = list[SignalPattern]
TranslationDict = dict[Wire, Segment]
Candidates = dict[Wire, set[Segment]]


SIGNAL_PATTERN_TO_DIGIT: dict[SignalPattern:int] = {
    frozenset("abcefg"): 0,
    frozenset("cf"): 1,
    frozenset("acdeg"): 2,
    frozenset("acdfg"): 3,
    frozenset("bcdf"): 4,
    frozenset("abdfg"): 5,
    frozenset("abdefg"): 6,
    frozenset("acf"): 7,
    frozenset("abcdefg"): 8,
    frozenset("abcdfg"): 9,
}

UNIQUE_SEGMENTS: dict[int, SignalPattern] = {
    1: set("cf"),
    4: set("bcdf"),
    7: set("acf"),
    8: set("abcdefg"),
}


def translate(pattern, translation_dict) -> frozenset[Segment]:
    return frozenset([translation_dict[wire] for wire in pattern])


def valid_translation(
    translation_dict: dict[Wire, Segment], patterns: list[SignalPattern]
) -> bool:
    for pattern in patterns:
        if translate(pattern, translation_dict) not in SIGNAL_PATTERN_TO_DIGIT.keys():
            return False
    return True


@dataclass
class Entry:
    signal_patterns: list[SignalPattern]
    output_value: OutputValue

    @classmethod
    def from_string(cls, text: str) -> Entry:
        signal_patterns, output_value = text.split(" | ")
        return cls(
            signal_patterns=[set(pattern) for pattern in signal_patterns.split()],
            output_value=[set(pattern) for pattern in output_value.split()],
        )

    def translated_output_value(self, translation: TranslationDict) -> int:
        digits: list[int] = []
        for value in self.output_value:
            digits.append(SIGNAL_PATTERN_TO_DIGIT[translate(value, translation)])

        return int("".join(str(digit) for digit in digits))


def parse_data(text: str) -> list[Entry]:
    entries = []
    for line in text.splitlines():
        entries.append(Entry.from_string(line))

    return entries


def get_unique_segment_lengths() -> set[int]:
    return {len(x) for x in UNIQUE_SEGMENTS.values()}


def part1(entries: list[Entry]) -> int:
    """Count number of output digits that contain "unique" number of segments"""
    unique_segment_lengths = get_unique_segment_lengths()

    count = 0
    for entry in entries:
        count += len(
            [
                digit
                for digit in entry.output_value
                if len(digit) in unique_segment_lengths
            ]
        )

    return count


def init_candidates() -> Candidates:
    return {s: set("abcdefg") for s in "abcdefg"}


def generate_translation_dicts(
    candidates: Candidates
) -> list[TranslationDict]:
    """The goal here is to generate all valid enumerations given a candidate dict

    e.g. if "a" could be b or c, then half of the results will have "a": "b" and the other half will be "a": "c"
    """
    results = []
    recurse_generate_translation_dicts(candidates, {}, results)
    return results


def recurse_generate_translation_dicts(
    _candidates: Candidates,
    translation_dict: TranslationDict,
    results: list[TranslationDict],
):
    """got lazy and/or tired so that's why I went with the mutable argument"""
    if not _candidates:
        results.append(translation_dict)
        return
    candidates = _candidates.copy()
    wire, segments = candidates.popitem()
    for segment in segments:
        if segment not in translation_dict.values():
            recurse_generate_translation_dicts(
                candidates, {**translation_dict, wire: segment}, results
            )


def part2(entries: list[Entry]) -> int:
    """
    Plan:
    For each entry:
        each wire starts with all segments as candidate position.
        eliminate based on unique patterns
        generate all possible translation candidates
        return the only valid one
    """
    results = []
    for entry in entries:
        candidates: dict[Wire, set[Segment]] = init_candidates()
        # first, narrow by unique lengths
        for signal_pattern in entry.signal_patterns:
            for unique_segment in UNIQUE_SEGMENTS.values():
                if len(signal_pattern) == len(unique_segment):
                    for wire in set("abcdefg"):
                        # we know that every wire in the signal pattern can only
                        # be controlling one of the segments in the unique pattern
                        if wire in signal_pattern:
                            candidates[wire] &= unique_segment
                        # we also know that the values in that unique segment can't exist anywhere else
                        else:
                            candidates[wire] -= unique_segment

        for candidate_translation in generate_translation_dicts(candidates):
            if valid_translation(candidate_translation, entry.signal_patterns):
                results.append(entry.translated_output_value(candidate_translation))
                break
    return sum(results)


def main():
    with open("input.txt") as f:
        entries = parse_data(f.read())
    print("Part 1", part1(entries))
    print("Part 2", part2(entries))


if __name__ == "__main__":
    main()
