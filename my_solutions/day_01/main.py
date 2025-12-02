from typing import cast, Literal

Direction = Literal["L", "R"]
Rotation = tuple[Direction, int]

DIAL_NUMBERS = 100
DIAL_START = 50


class DayPuzzleSolver:
    def __init__(self):
        self.delimiter = "\n"

    def solve_part_1(self, raw_input: list[str]):
        rotations = self.process_input(raw_input)
        return self.find_number_of_times_stopping_at_0(rotations)

    def solve_part_2(self, raw_input: list[str]):
        rotations = self.process_input(raw_input)
        return self.find_number_of_times_passing_through_0(rotations)

    def process_input(self, raw_input: list[str]) -> list[Rotation]:
        return [(cast(Direction, line[0]), int(line[1:])) for line in raw_input]

    def find_number_of_times_stopping_at_0(self, rotations: list[Rotation]):
        times_at_0 = 0
        dial_number = DIAL_START

        for rotation in rotations:
            dial_number = self.rotate(dial_number, rotation)
            dial_number %= DIAL_NUMBERS

            if dial_number == 0:
                times_at_0 += 1

        return times_at_0

    def find_number_of_times_passing_through_0(self, rotations: list[Rotation]):
        times_at_0 = 0
        dial_number = DIAL_START
        last_dial_number = None

        for rotation in rotations:
            dial_number = self.rotate(dial_number, rotation)

            if dial_number == 0:
                times_at_0 += 1
            elif dial_number >= DIAL_NUMBERS:
                times_at_0 += dial_number // DIAL_NUMBERS
            elif dial_number < 0:
                times_at_0 += -dial_number // DIAL_NUMBERS + (
                    0 if last_dial_number == 0 else 1
                )

            dial_number %= DIAL_NUMBERS
            last_dial_number = dial_number

        return times_at_0

    def rotate(self, dial_number: int, rotation: Rotation) -> int:
        direction, distance = rotation
        if direction == "R":
            return dial_number + distance
        return dial_number - distance
