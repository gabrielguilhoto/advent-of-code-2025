from typing import Literal, cast

Matrix = list[list[int | None]]
Operator = Literal["+", "*"]

MAX_OPERANDS = 4


class DayPuzzleSolver:
    def __init__(self):
        self.delimiter = "\n"

    def solve_part_1(self, raw_input: list[str]) -> int:
        number_matrix, operators = self.process_input_for_part_1(raw_input)
        return self.solve_worksheet(number_matrix, operators)

    def solve_part_2(self, raw_input: list[str]) -> int:
        number_matrix, operators = self.process_input_for_part_2(raw_input)
        return self.solve_worksheet(number_matrix, operators)

    def process_input_for_part_1(self, raw_input: list[str]) -> tuple[Matrix, list[Operator]]:
        number_matrix: Matrix = [
            [int(raw_num) for raw_num in line.split()] for line in raw_input[:-1]
        ]
        operators: list[Operator] = [cast(Operator, op) for op in raw_input[-1].split()]

        return number_matrix, operators

    def process_input_for_part_2(self, raw_input: list[str]) -> tuple[Matrix, list[Operator]]:
        operators: list[Operator] = [cast(Operator, op) for op in raw_input[-1].split()]
        number_matrix: Matrix = [[None] * len(operators) for _ in range(MAX_OPERANDS)]

        problem_index = 0
        operand_index = 0
        for j in range(len(raw_input[0])):
            raw_number = "".join([raw_input[i][j] for i in range(len(raw_input) - 1)])

            if raw_number.isspace():  # no numbers, problem has ended
                problem_index += 1
                operand_index = 0
                continue

            number_matrix[operand_index][problem_index] = int(raw_number)
            operand_index += 1

        return number_matrix, operators

    def solve_worksheet(self, number_matrix: Matrix, operators: list[Operator]) -> int:
        return sum(
            self.solve_problem(number_matrix, operators[j], j) for j in range(len(operators))
        )

    def solve_problem(self, number_matrix: Matrix, operator: Operator, j: int) -> int:
        answer = 0 if operator == "+" else 1

        for i in range(len(number_matrix)):
            number = number_matrix[i][j]
            if number is not None:
                answer = self.make_operation(answer, operator, number)

        return answer

    def make_operation(self, a: int, operator: Operator, b: int) -> int:
        if operator == "+":
            return a + b
        return a * b
