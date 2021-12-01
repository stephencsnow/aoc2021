defmodule Day1 do
  def parse_input(filename) do
    File.read!(filename)
    |> String.split("\n", trim: true)
    |> Enum.map(&String.to_integer/1)
  end

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

  def main do
    parse_input("input.txt")
    |> count_increases
  end
end
