from day10.syntax import part1, get_first_illegal_character


def fixture() -> list[str]:
    text = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""
    return text.splitlines()


def test_get_first_illegal_character():
    assert get_first_illegal_character("{([(<{}[<>[]}>{[]{[(<()>") == "}"
    assert get_first_illegal_character("[[<[([]))<([[{}[[()]]]") == ")"
    assert get_first_illegal_character("[({(<(())[]>[[{[]{<()<>>") is None


def test_part1():
    assert part1(fixture()) == 26397
