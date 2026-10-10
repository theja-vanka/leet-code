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
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    _r, _c = row + dr, col + dc
                    if (_r in range(rows) and _c in range(cols) and
                    grid[_r][_c] == "1" and
                    (_r, _c) not in visit):
                        q.append((_r,_c))
                        visit.add((_r, _c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r,c)
                    islands += 1

        return islands