from typing import Generator, Iterable

Range = tuple[int, int]
MAX_DIGITS = 10


class DayPuzzleSolver:
    def __init__(self):
        self.delimiter = ""

    def solve_part_1(self, raw_input: str):
        ranges = self.process_raw_input(raw_input)
        invalid_ids = self.generate_all_invalid_ids_for_part_1(MAX_DIGITS)

        return self.sum_ids_in_ranges(invalid_ids, ranges)

    def solve_part_2(self, raw_input: str):
        ranges = self.process_raw_input(raw_input)
        invalid_ids = self.generate_all_invalid_ids_for_part_2(MAX_DIGITS)

        return self.sum_ids_in_ranges(invalid_ids, ranges)

    def process_raw_input(self, raw_input: str) -> list[Range]:
        result: list[Range] = []

        for raw_range in raw_input.split(","):
            start, end = raw_range.split("-")
            result.append((int(start), int(end)))

        return result

    def generate_all_invalid_ids_for_part_1(
        self, max_digits: int
    ) -> Generator[int, None, None]:
        for i in range(1, 10 ** (max_digits // 2)):
            yield int(f"{i}{i}")

    def generate_all_invalid_ids_for_part_2(self, max_digits: int) -> set[int]:
        invalid_ids: set[int] = set()

        for i in range(1, 10 ** (max_digits // 2)):
            id = f"{i}{i}"
            while len(id) <= max_digits:
                invalid_ids.add(int(id))
                id += str(i)

        return invalid_ids

    def sum_ids_in_ranges(self, ids: Iterable[int], ranges: list[Range]) -> int:
        return sum(id for id in ids if self.is_id_in_ranges(id, ranges))

    def is_id_in_ranges(self, id: int, ranges: list[Range]):
        for range in ranges:
            start, end = range
            if start <= id <= end:
                return True
            
        return False
