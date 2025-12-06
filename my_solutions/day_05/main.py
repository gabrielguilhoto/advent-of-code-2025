Range = tuple[int, int]


class DayPuzzleSolver:
    def __init__(self):
        self.delimiter = "\n"

    def solve_part_1(self, raw_input: list[str]) -> int:
        fresh_id_ranges, ingredient_ids = self.process_input(raw_input)
        return sum(
            1
            for ingredient_id in ingredient_ids
            if self.is_ingredient_fresh(ingredient_id, fresh_id_ranges)
        )

    def solve_part_2(self, raw_input: list[str]) -> int:
        id_ranges, _ = self.process_input(raw_input)
        return self.count_ids_in_ranges(id_ranges)

    def process_input(self, raw_input: list[str]) -> tuple[list[Range], list[int]]:
        fresh_id_ranges: list[Range] = []
        ingredient_ids: list[int] = []

        for line in raw_input:
            splitted_line = line.split("-")

            if len(splitted_line) == 2:
                start, end = splitted_line
                fresh_id_ranges.append((int(start), int(end)))
            elif len(splitted_line) == 1 and line:
                ingredient_ids.append(int(line))

        return fresh_id_ranges, ingredient_ids

    def is_ingredient_fresh(
        self, ingredient_id: int, fresh_id_ranges: list[Range]
    ) -> bool:
        for start, end in fresh_id_ranges:
            if start <= ingredient_id <= end:
                return True

        return False

    def count_ids_in_ranges(self, id_ranges: list[Range]) -> int:
        id_ranges.sort()
        id_count = 0
        last_range_end = 0

        for start, end in id_ranges:
            if end <= last_range_end:
                continue

            new_ids_start = max(start, last_range_end + 1)
            id_count += end - new_ids_start + 1
            last_range_end = end

        return id_count
