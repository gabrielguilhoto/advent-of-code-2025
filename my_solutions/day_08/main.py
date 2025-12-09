import collections
import math

Position = tuple[int, int, int]
Distances = list[tuple[float, int, int]]


class DisjointSets:
    def __init__(self, N: int) -> None:
        self.N = N
        self.parent = [i for i in range(N)]

    def union(self, x: int, y: int) -> None:
        self.parent[self.find(x)] = self.find(self.parent[y])

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def get_set_sizes(self) -> list[int]:
        size_by_representative: dict[int, int] = collections.defaultdict(int)
        for i in range(self.N):
            size_by_representative[self.find(i)] += 1
        return list(size_by_representative.values())


class DayPuzzleSolver:
    def __init__(self):
        self.delimiter = "\n"

    def solve_part_1(self, raw_input: list[str]) -> int:
        positions = self.parse_input(raw_input)
        distances = self.calculate_pairwise_distances(positions)

        N = len(positions)
        ds = self.connect_closest_boxes(N, distances, 1000 if N > 100 else 10)
        return self.get_multiplied_size_of_3_largest_circuits(ds)

    def solve_part_2(self, raw_input: list[str]) -> int:
        positions = self.parse_input(raw_input)
        distances = self.calculate_pairwise_distances(positions)

        i, j = self.connect_all_boxes(len(positions), distances)
        return positions[i][0] * positions[j][0]

    def parse_input(self, raw_input: list[str]) -> list[Position]:
        positions: list[Position] = []
        for line in raw_input:
            x, y, z = line.split(",")
            positions.append((int(x), int(y), int(z)))
        return positions

    def calculate_pairwise_distances(self, positions: list[Position]) -> Distances:
        return sorted(
            [
                (self.calculate_distance(p1, p2), i, j)
                for i, p1 in enumerate(positions)
                for j, p2 in enumerate(positions)
                if i < j
            ]
        )

    def calculate_distance(self, p1: Position, p2: Position) -> float:
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)

    def connect_closest_boxes(
        self, N: int, distances: Distances, connection_limit: int
    ) -> DisjointSets:
        ds = DisjointSets(N)

        for _, i, j in distances[:connection_limit]:
            ds.union(i, j)

        return ds

    def connect_all_boxes(self, N: int, distances: Distances) -> tuple[int, int]:
        ds = DisjointSets(N)
        connection_count = 0

        for _, i, j in distances:
            if ds.find(i) != ds.find(j):
                ds.union(i, j)
                connection_count += 1
                if connection_count == N - 1:
                    return i, j

        raise ValueError("Boxes are not connectable")

    def get_multiplied_size_of_3_largest_circuits(self, ds: DisjointSets) -> int:
        return math.prod(sorted(ds.get_set_sizes(), reverse=True)[:3])
