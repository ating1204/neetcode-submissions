class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        
        visited = set()
        print(visited)
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                
                for d1, d2 in directions:
                    x, y = row + d1, col + d2
                    if (x in range(rows) and 
                        y in range(cols) and
                        grid[x][y] == "1" and 
                        (x,y) not in visited):
                        q.append((x, y))
                        visited.add((x,y))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r,c)
                    islands += 1

        return islands