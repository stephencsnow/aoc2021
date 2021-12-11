defmodule Day2Test do
  use ExUnit.Case
  doctest Day2

  test "greets the world" do
    txt = "
    forward 5
    down 5
    forward 8
    up 3
    down 8
    forward 2"
    data = txt
    |> String.split("\n", trim: true)
    |> Enum.map(&String.trim/1)
    |> Enum.map(&String.split/1)
    |> Enum.map(fn [dir, amount] -> {String.to_atom(dir), String.to_integer(amount)} end)

    assert Day2.get_xy(data, {0, 0}) == {15, 10}
  end
end
