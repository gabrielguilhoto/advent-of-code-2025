class DayPuzzleSolver:
    def __init__(self):
        self.delimiter = "\n"

    def solve_part_1(self, banks: list[str]):
        return sum([self.find_max_joltage_with_k_batteries(bank, 2) for bank in banks])

    def solve_part_2(self, banks: list[str]):
        return sum([self.find_max_joltage_with_k_batteries(bank, 12) for bank in banks])

    def find_max_joltage_with_k_batteries(self, bank: str, k: int) -> int:
        picked_battery_positions: list[int] = []
        previous_position = -1

        for i in range(k):
            search_range = (previous_position + 1, len(bank) - k + i)
            battery_position = self.find_argmax_joltage(bank, search_range)

            picked_battery_positions.append(battery_position)
            previous_position = battery_position

        picked_batteries = [bank[position] for position in picked_battery_positions]
        return int("".join(picked_batteries))

    def find_argmax_joltage(self, bank: str, search_range: tuple[int, int]) -> int:
        (start, end) = search_range
        argmax = -1
        max_joltage = "0"

        for i in range(start, end + 1):
            if bank[i] > max_joltage:
                argmax = i
                max_joltage = bank[i]

        return argmax
