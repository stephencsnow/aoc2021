defmodule Day3 do
  def parse_input(filename) do
    File.read!(filename)
    |> String.split("\n", trim: true)
    |> Enum.map(fn line -> String.split(line, "", trim: true) |> Enum.map(&String.to_integer/1) end)
  end

  defp transpose(list_of_lists) do
    list_of_lists
    |> List.zip()
    |> Enum.map(&Tuple.to_list/1)
  end

  defp times_one_appears(list), do: Enum.sum(list)
  defp one_is_most_common?(list), do: times_one_appears(list) > Enum.count(list) / 2

  def most_common_bit(list) do
    case one_is_most_common?(list) do
      true -> 1
      false -> 0
    end
  end

  def least_common_bit(list) do
    case one_is_most_common?(list) do
      true -> 0
      false -> 1
    end
  end

  def gamma(list_of_lists) do
    list_of_lists
    |> transpose
    |> Enum.map(&most_common_bit/1)
    |> Integer.undigits(2)
  end

  def epsilon(list_of_lists) do
    list_of_lists
    |> transpose
    |> Enum.map(&least_common_bit/1)
    |> Integer.undigits(2)
  end

  def power_consumption(list_of_lists), do: gamma(list_of_lists) * epsilon(list_of_lists)

  def part1 do
    parse_input("input.txt")
    |> power_consumption
  end
end
