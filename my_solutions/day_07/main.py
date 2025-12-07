import functools

Map = list[str]
Position = tuple[int, int]

SPLITTER = "^"
START = "S"


class DayPuzzleSolver:
    def __init__(self):
        self.delimiter = "\n"

    def solve_part_1(self, map: Map) -> int:
        return self.count_splits(map, self.find_start_position(map), set())

    def solve_part_2(self, map: Map) -> int:
        self.map = map
        return self.count_timelines(self.find_start_position(map))

    def find_start_position(self, map: Map) -> Position:
        return next((0, j) for j in range(len(map[0])) if map[0][j] == START)

    def count_splits(self, map: Map, position: Position, visited: set[Position]) -> int:
        visited.add(position)

        (i, j) = position
        split_count = 1 if map[i][j] == SPLITTER else 0

        for neighbor in self.get_neighbors(map, position):
            if neighbor not in visited:
                split_count += self.count_splits(map, neighbor, visited)

        return split_count

    @functools.cache
    def count_timelines(self, position: Position) -> int:
        neighbors = self.get_neighbors(self.map, position)
        if not neighbors:
            return 1

        return sum(self.count_timelines(neighbor) for neighbor in neighbors)

    def get_neighbors(self, map: Map, position: Position) -> list[Position]:
        (i, j) = position
        if map[i][j] == SPLITTER:
            neighbors = [(i, j - 1), (i, j + 1)]
        else:
            neighbors = [(i + 1, j)]

        return [
            (i_n, j_n) for (i_n, j_n) in neighbors if 0 <= i_n < len(map) and 0 <= j_n < len(map[i])
        ]
