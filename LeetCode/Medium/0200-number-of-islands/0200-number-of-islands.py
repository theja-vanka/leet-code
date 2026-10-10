class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0
        if not grid:
            return islands

        rows, cols = len(grid), len(grid[0])
        visit = set()

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            while q:
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                row, col = q.popleft()
                for dr, dc in directions:
                    _r, _c = row + dr, col + dc
                    if (0 <= _r < rows and
                        0 <= _c < cols and
                        grid[_r][_c] == "1" and
                        (_r, _c) not in visit):
                            visit.add((_r, _c))
                            q.append((_r, _c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        
        return islands