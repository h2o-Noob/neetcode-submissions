class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        res = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):
            visited.add((i, j))
            nonlocal count 
            count += 1

            for di, dj in directions:
                ni, nj = di + i, dj + j

                if 0 <= ni < rows and 0 <= nj < cols and (ni, nj) not in visited and grid[ni][nj] == 1:
                    dfs(ni, nj)
        

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == 1:
                    dfs(i, j)
                    res = max(count, res)
                    count = 0
        
        return res



        
        