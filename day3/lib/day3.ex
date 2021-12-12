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

  def most_common_bit(list, tiebreak \\ 1) do
    len = Enum.count(list)
    ones = times_one_appears(list)
    cond do
      ones > len / 2 -> 1
      ones == len / 2 -> tiebreak
      true -> 0
    end
  end

  def least_common_bit(list, tiebreak \\ 0) do
    len = Enum.count(list)
    ones = times_one_appears(list)
    cond do
      ones > len / 2 -> 0
      ones == len / 2 -> tiebreak
      true -> 1
    end
  end

  def st_common_bit(list, :most), do: most_common_bit(list)
  def st_common_bit(list, :least), do: least_common_bit(list)

  defp only_st_bits(list_of_lists, st) do
    list_of_lists
    |> transpose
    |> Enum.map(fn list -> st_common_bit(list, st) end)
    |> Integer.undigits(2)
  end

  def gamma(list_of_lists), do: only_st_bits(list_of_lists, :most)

  def epsilon(list_of_lists), do: only_st_bits(list_of_lists, :least)


  def power_consumption(list_of_lists), do: gamma(list_of_lists) * epsilon(list_of_lists)

  defp recurse(list_of_lists, st_bit, leading_bits \\ [])

  defp recurse([last_value], _, leading_bits) do
    leading_bits ++ last_value
    |> Integer.undigits(2)
  end

  defp recurse(list_of_lists, st_bit, leading_bits) do
    desired_bit =
      list_of_lists
      |> transpose
      |> List.first
      |> st_common_bit(st_bit)

    remaining_elements =
      list_of_lists
      |> Enum.map(fn list -> List.pop_at(list, 0) end)
      |> Enum.filter(fn {bit, _} -> bit == desired_bit end)
      |> Enum.map(fn {_, remaining} -> remaining end)

    recurse(remaining_elements, st_bit, leading_bits ++ [desired_bit])
  end

  def oxygen_generator_rating(list_of_lists) do
    recurse(list_of_lists, :most)
  end

  def co2_scrubber_rating(list_of_lists) do
    recurse(list_of_lists, :least)
  end

  def life_support_rating(list_of_lists), do: oxygen_generator_rating(list_of_lists) * co2_scrubber_rating(list_of_lists)

  def part1 do
    parse_input("input.txt")
    |> power_consumption
  end

  def part2 do
    parse_input("input.txt")
    |> life_support_rating
  end
end
