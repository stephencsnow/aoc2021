from collections import Counter

Timer = int

TIME_TO_CREATE = 0
RESET_TIMER = 6
INITIAL_TIMER = 8


def parse_data(text: str) -> list[Timer]:
    return [int(timer) for timer in text.split(",")]


def cycle(timers: list[Timer], steps: int) -> int:
    counter = Counter(timers)

    for step in range(steps):
        new_counter = Counter()
        for timer, num_fish in counter.items():
            if timer == TIME_TO_CREATE:
                # fish getting ready to create again
                new_counter[RESET_TIMER] += num_fish
                # new fish being born
                new_counter[INITIAL_TIMER] += num_fish
            else:
                new_counter[timer - 1] += num_fish

        counter = new_counter

    return sum(counter.values())


def main():
    with open("input.txt") as f:
        timers = parse_data(f.read())
    print("Part 1", cycle(timers, 80))
    print("Part 2", cycle(timers, 256))


if __name__ == "__main__":
    main()
