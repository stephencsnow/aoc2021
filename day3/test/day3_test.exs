defmodule Day3Test do
  use ExUnit.Case
  doctest Day3

  test "part 1" do
    txt = "
      00100
      11110
      10110
      10111
      10101
      01111
      00111
      11100
      10000
      11001
      00010
      01010"

    data = txt
    |> String.split("\n", trim: true)
    |> Enum.map(&String.trim/1)
    |> Enum.map(fn line -> String.split(line, "", trim: true) |> Enum.map(&String.to_integer/1) end)

    assert Day3.gamma(data) == 22
    assert Day3.epsilon(data) == 9
    assert Day3.power_consumption(data) == 198
  end

  test "part 2" do
    txt = "
      00100
      11110
      10110
      10111
      10101
      01111
      00111
      11100
      10000
      11001
      00010
      01010"

    data = txt
    |> String.split("\n", trim: true)
    |> Enum.map(&String.trim/1)
    |> Enum.map(fn line -> String.split(line, "", trim: true) |> Enum.map(&String.to_integer/1) end)

    assert Day3.oxygen_generator_rating(data) == 23
    assert Day3.co2_scrubber_rating(data) == 10
    assert Day3.life_support_rating(data) == 230
  end
end
