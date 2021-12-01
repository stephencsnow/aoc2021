defmodule Day1Test do
  use ExUnit.Case
  doctest Day1

  test "sliding window of 1" do
    txt = "199
    200
    208
    210
    200
    207
    240
    269
    260
    263"
    data = txt
      |> String.split("\n", trim: true)
      |> Enum.map(&String.trim/1)
      |> Enum.map(&String.to_integer/1)

    assert Day1.count_increases_sliding_window(data, 1) == 7
  end

  test "sliding window of 3" do
    txt = "199
    200
    208
    210
    200
    207
    240
    269
    260
    263"
    data = txt
      |> String.split("\n", trim: true)
      |> Enum.map(&String.trim/1)
      |> Enum.map(&String.to_integer/1)

    assert Day1.count_increases_sliding_window(data, 3) == 5
  end
end
