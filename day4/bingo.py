from copy import deepcopy
from typing import Any, List, Tuple, TypeVar

T = TypeVar("T")


def _init_array(n_rows: int, n_cols: int, init_value: T) -> List[List[T]]:
    result = []
    for n in range(n_rows):
        result.append([init_value] * n_cols)
    return result


def transpose(matrix: List[List[T]]) -> List[List[T]]:
    return [list(x) for x in zip(*matrix)]


class BingoBoard:
    data: List[List[int]]
    marked: List[List[bool]]

    def __init__(self, data: List[List[int]]):
        self.data = data
        self.marked = _init_array(
            n_rows=len(data), n_cols=len(data[0]), init_value=False
        )

    @classmethod
    def from_string(cls, board_string: str) -> "BingoBoard":
        data = []
        for row in board_string.splitlines():
            data.append([int(x) for x in row.strip().split()])

        return cls(data)

    def mark(self, drawn_number: int) -> bool:
        for i, row in enumerate(self.data):
            for j, value in enumerate(row):
                if value == drawn_number:
                    self.marked[i][j] = True
                    return True
        return False

    @staticmethod
    def _check_horizontals(matrix) -> bool:
        for row in matrix:
            for value in row:
                if not value:
                    break
            else:
                return True
        return False

    def thats_a_bingo(self) -> bool:
        # first, check rows
        if self._check_horizontals(self.marked):
            return True
        # second, check columns
        if self._check_horizontals(transpose(self.marked)):
            return True

        return False

    def _sum_of_all_unmarked_numbers(self) -> int:
        sum = 0
        for i, row in enumerate(self.data):
            for j, value in enumerate(row):
                if not self.marked[i][j]:
                    sum += value
        return sum

    def score(self, last_called_number: int) -> int:
        return self._sum_of_all_unmarked_numbers() * last_called_number


def parse_input(txt: str) -> Tuple[List[int], List[BingoBoard]]:
    values = txt.strip().split("\n\n")

    drawn_numbers = [int(x) for x in values[0].split(",")]

    bingo_boards = [BingoBoard.from_string(board_string) for board_string in values[1:]]

    return drawn_numbers, bingo_boards


def part1(numbers: List[int], boards: List[BingoBoard]) -> int:
    for number in numbers:
        for board in boards:
            board.mark(number)

        winning_boards = [board for board in boards if board.thats_a_bingo()]
        if any(winning_boards):
            return winning_boards[0].score(number)


def part2(numbers: List[int], boards: List[BingoBoard]) -> int:
    boards_in_play = deepcopy(boards)
    for number in numbers:
        for board in boards_in_play:
            board.mark(number)

        winning_boards = [board for board in boards_in_play if board.thats_a_bingo()]
        if winning_boards:
            if len(boards_in_play) == 1:
                # last winning board
                return winning_boards[0].score(number)
            else:
                for board in winning_boards:
                    boards_in_play.remove(board)


def main():
    with open("input.txt") as f:
        numbers, boards = parse_input(f.read())
    print(f"Part 1: {part1(numbers, boards)}")
    print(f"Part 2: {part2(numbers, boards)}")


if __name__ == "__main__":
    main()
