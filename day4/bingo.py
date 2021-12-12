from __future__ import annotations
from copy import deepcopy
from typing import Any, Generator, Generic, List, TypeVar


T = TypeVar("T")


class TwoDArray(Generic[T]):
    _data: list[T]
    n_rows: int
    n_columns: int
    _idx: int

    def __init__(
        self,
        data: list[T],
        n_rows: int,
        n_columns: int,
    ) -> None:
        self._data = data
        self.n_rows = n_rows
        self.n_columns = n_columns

    def __getitem__(self, row_index: int) -> list[T]:
        """Slice over the range of the desired row"""
        return self._data[row_index * self.n_columns : (row_index + 1) * self.n_columns]

    def __iter__(self):
        self._idx = 0
        return self

    def __next__(self):
        if self._idx >= self.n_rows * self.n_columns:
            raise StopIteration
        val = self._data[self._idx]
        self._idx += 1
        return val

    def __repr__(self) -> str:
        return str(list(self.rows))

    @property
    def rows(self) -> Generator[list[T], None, None]:
        for i in range(self.n_rows):
            yield self[i]

    @property
    def columns(self) -> Generator[list[T], None, None]:
        for j in range(self.n_columns):
            yield [x for idx, x in enumerate(self._data) if idx % self.n_columns == j]


class BingoBoard:
    data: TwoDArray[int]
    marked: set[int]

    def __init__(self, data: list[int], dim: int):
        self.data = TwoDArray(data, n_rows=dim, n_columns=dim)
        self.marked = set()

    @classmethod
    def from_string(cls, board_string: str) -> BingoBoard:
        dim = len(board_string.strip().splitlines())
        return cls([int(x) for x in board_string.strip().split()], dim)

    def call_number(self, drawn_number: int) -> None:
        self.marked.add(drawn_number)

    def thats_a_bingo(self) -> bool:
        # check rows
        for row in self.data.rows:
            if all(value in self.marked for value in row):
                return True

        # check columns
        for column in self.data.columns:
            if all(value in self.marked for value in column):
                return True

        return False

    def _sum_of_all_unmarked_numbers(self) -> int:
        sum = 0
        for val in self.data:
            if val not in self.marked:
                sum += val
        return sum

    def score(self, last_called_number: int) -> int:
        return self._sum_of_all_unmarked_numbers() * last_called_number


def parse_input(txt: str) -> tuple[list[int], list[BingoBoard]]:
    values = txt.strip().split("\n\n")

    drawn_numbers = [int(x) for x in values[0].split(",")]

    bingo_boards = [BingoBoard.from_string(board_string) for board_string in values[1:]]

    return drawn_numbers, bingo_boards


def part1(numbers: list[int], boards: list[BingoBoard]) -> int:
    for number in numbers:
        for board in boards:
            board.call_number(number)

        winning_boards = [board for board in boards if board.thats_a_bingo()]
        if any(winning_boards):
            return winning_boards[0].score(number)

    raise AssertionError


def part2(numbers: list[int], boards: list[BingoBoard]) -> int:
    boards_in_play = deepcopy(boards)
    for number in numbers:
        for board in boards_in_play:
            board.call_number(number)

        winning_boards = [board for board in boards_in_play if board.thats_a_bingo()]
        if winning_boards:
            if len(boards_in_play) == 1:
                # last winning board
                return winning_boards[0].score(number)
            else:
                for board in winning_boards:
                    boards_in_play.remove(board)

    raise AssertionError


def main():
    with open("input.txt") as f:
        numbers, boards = parse_input(f.read())
    print(f"Part 1: {part1(numbers, boards)}")
    print(f"Part 2: {part2(numbers, boards)}")


if __name__ == "__main__":
    main()
