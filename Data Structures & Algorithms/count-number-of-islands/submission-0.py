class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        
        def dp(i, j):

            visited.add((i,j))

            for di, dj in directions:
                ni, nj = di + i, dj + j
            
                if 0 <= ni < rows and 0 <= nj < cols and (ni, nj) not in visited and grid[ni][nj] == '1':
                    dp(ni, nj)
        
        count = 0

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == '1':
                    dp(i,j)
                    count = count + 1
        
        return count
        
        
            

        

        
            



        