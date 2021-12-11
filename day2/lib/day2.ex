defmodule Day2 do
  def parse_input(filename) do
    File.read!(filename)
    |> String.split("\n", trim: true)
    |> Enum.map(&String.split/1)
    |> Enum.map(fn [dir, amount] -> {String.to_atom(dir), String.to_integer(amount)} end)
  end

  def get_xy(movements, current_position)
  def get_xy([], {x, y}), do: {x, y}
  def get_xy([{:forward, amount} | rest], {x, y}), do: get_xy(rest, {x + amount, y})
  def get_xy([{:down, amount} | rest], {x, y}), do: get_xy(rest, {x, y + amount})
  def get_xy([{:up, amount} | rest], {x, y}), do: get_xy(rest, {x, y - amount})

  def part1 do
    {x, y}=
      parse_input("input.txt")
      |> get_xy({0, 0})

    x * y
  end
end
