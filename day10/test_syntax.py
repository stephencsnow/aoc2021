from day10.syntax import part1, get_first_illegal_character, part2, get_completion_string


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


def test_get_completion_string():
    assert get_completion_string("[({(<(())[]>[[{[]{<()<>>") == "}}]])})]"
    assert get_completion_string("[(()[<>])]({[<{<<[]>>(") == ")}>]})"

def test_part2():
    assert part2(fixture()) == 288957
