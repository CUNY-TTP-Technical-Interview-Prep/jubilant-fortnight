from typing import List


def closedIsland(self, grid: List[List[int]]) -> int:
    seen_land = set()

    def bfs(i: int, j: int) -> int:
        seen_land.add((i, j))
        q, ans = [(i, j)], 1
        for i, j in q:
            for r, c in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                    ans = 0
                elif not grid[r][c] and (r, c) not in seen_land:
                    seen_land.add((r, c))
                    q.append((r, c))
        return ans

    return sum(bfs(i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if not cell and (i, j) not in seen_land)
