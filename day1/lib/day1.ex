defmodule Day1 do
  def parse_input(filename) do
    File.read!(filename)
    |> String.split("\n", trim: true)
    |> Enum.map(&String.to_integer/1)
  end

  # part 1
  def count_increases(report) do
    [first_depth | rest] = report
    {total_increases, _} = Enum.reduce(rest, {0, first_depth}, fn depth, {num_increases, prev_depth} ->
      cond do
        depth > prev_depth -> {num_increases + 1, depth}
        true -> {num_increases, depth}
      end
    end)
    total_increases
  end

  # part 2
  def count_increases_sliding_window(report, window_size) do
    {init_window, rest} = Enum.split(report, window_size)

    {total_increases, _} = Enum.reduce(rest, {0, init_window}, fn depth, {num_increases, prev_window} ->
      [_ | remaining] = prev_window
      new_window = remaining ++ [depth]
      cond do
        Enum.sum(new_window) > Enum.sum(prev_window) -> {num_increases + 1, new_window}
        true -> {num_increases, new_window}
      end
    end)
    total_increases
  end

  def part1 do
    parse_input("input.txt")
    |> count_increases_sliding_window(1)
  end

  def part2 do
    parse_input("input.txt")
    |> count_increases_sliding_window(3)
  end
end
