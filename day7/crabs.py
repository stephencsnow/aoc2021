from typing import Callable

Position = int
Fuel = int


def fuel_cost(positions: list[Position], position_to_move_to: Position) -> Fuel:
    total_fuel = 0
    for position in positions:
        total_fuel += abs(position - position_to_move_to)

    return total_fuel


def get_fuel_costs(positions: list[Position]) -> dict[Position, Fuel]:
    costs = {}
    for position in range(min(positions), max(positions) + 1):
        costs[position] = fuel_cost(positions, position)

    return costs


def gradient_descent(
    positions: list[Position],
    current_position: Position,
    function: Callable[[list[Position], Position], Fuel],
) -> Position:
    one_below = function(positions, current_position - 1)
    current_value = function(positions, current_position)
    one_above = function(positions, current_position + 1)

    match one_below, current_value, one_above:
        case _, current_value, _ if one_below > current_value < one_above:
            return current_position
        case _, current_value, _ if one_below < current_value:
            return gradient_descent(positions, current_position - 1, function)
        case _, current_value, _ if one_above < current_value:
            return gradient_descent(positions, current_position + 1, function)
        case _:
            raise AssertionError("unhandled")


def part1(positions: list[Position]) -> int:
    """
    Gradient descent approach here.
    Start with the average value, then move in the direction of fuel cost being lower.

    Assumes that local minima == local maxima
    """
    # start with mean
    initial_position = int(sum(positions) / len(positions))
    optimal_position = gradient_descent(positions, initial_position, fuel_cost)

    return fuel_cost(positions, optimal_position)


def main():
    with open("input.txt") as f:
        positions = [int(x) for x in f.read().split(",")]
    print("Part 1", part1(positions))


if __name__ == "__main__":
    main()
