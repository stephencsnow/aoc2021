from collections import deque

OPENING_CHARACTERS = ("(", "[", "{", "<")
CLOSING_CHARACTERS = (")", "]", "}", ">")

CHARACTER_PAIRS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def get_first_illegal_character(line: str) -> str | None:
    """Get first illegal character in a line if it exists, else None

    Illegal character is defined as an ill timed closing character
    """
    # stack based solution
    # we store closing characters on a stack
    stack = []
    for character in line:
        if character in OPENING_CHARACTERS:
            stack.append(CHARACTER_PAIRS[character])
        elif not stack:
            return character
        else:
            expected_character = stack.pop()
            if character != expected_character:
                return character

    return None


def part1(lines: list[str]) -> int:
    """Find total syntax error score

    Each character has different score
    A syntax error is one where an incorrect closing character is used
    """
    illegal_characters: list[str] = []
    for line in lines:
        if first_illegal_character := get_first_illegal_character(line):
            # line is corrupted
            illegal_characters.append(first_illegal_character)

    return sum(SCORES[char] for char in illegal_characters)


def main():
    with open("input.txt") as f:
        data = f.read().splitlines()
    print("Part 1: ", part1(data))
    # print("Part 2: ", part2(data))


if __name__ == "__main__":
    main()
