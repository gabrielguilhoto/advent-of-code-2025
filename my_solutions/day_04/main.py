Grid = list[str]
Cell = tuple[int, int]


class DayPuzzleSolver:
    def __init__(self):
        self.delimiter = "\n"

    def solve_part_1(self, grid: Grid) -> int:
        return sum(
            1 for count in self.count_neighbor_rolls_by_cell(grid).values() if count < 4
        )

    def solve_part_2(self, grid: Grid) -> int:
        neighbor_rolls_by_cell = self.count_neighbor_rolls_by_cell(grid)
        removable_roll_cells = {
            cell for cell, count in neighbor_rolls_by_cell.items() if count < 4
        }
        removed_roll_count = 0

        while removable_roll_cells:
            self.remove_roll(grid, neighbor_rolls_by_cell, removable_roll_cells)
            removed_roll_count += 1

        return removed_roll_count

    def count_neighbor_rolls_by_cell(self, grid: Grid) -> dict[Cell, int]:
        return {
            (i, j): len(self.get_neighbor_roll_cells(grid, i, j))
            for i in range(len(grid))
            for j in range(len(grid[i]))
            if grid[i][j] == "@"
        }

    def get_neighbor_roll_cells(self, grid: Grid, i: int, j: int) -> list[Cell]:
        N = len(grid)
        M = len(grid[0])

        return [
            (i_n, j_n)
            for (i_n, j_n) in [
                (i - 1, j - 1),
                (i - 1, j),
                (i - 1, j + 1),
                (i, j - 1),
                (i, j + 1),
                (i + 1, j - 1),
                (i + 1, j),
                (i + 1, j + 1),
            ]
            if 0 <= i_n < N and 0 <= j_n < M and grid[i_n][j_n] == "@"
        ]

    def remove_roll(
        self,
        grid: Grid,
        neighbor_rolls_by_cell: dict[Cell, int],
        removable_roll_cells: set[Cell],
    ) -> None:
        (i, j) = removable_roll_cells.pop()

        for neighbor in self.get_neighbor_roll_cells(grid, i, j):
            neighbor_rolls_by_cell[neighbor] -= 1

            if neighbor_rolls_by_cell[neighbor] == 3:
                removable_roll_cells.add(neighbor)
