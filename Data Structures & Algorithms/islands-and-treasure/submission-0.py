class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        visited = set()
        rows, cols = len(grid), len(grid[0])
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        q = deque()

        def addN(i, j):
            for di, dj in direction:
                ni, nj = di + i, dj + j

                if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] != -1 and (ni, nj) not in visited:
                    q.append([ni, nj])
                    visited.add((ni, nj))
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append([i, j])
                    visited.add((i, j))
        
        dist = 0

        while q:

            for n in range(len(q)):
                i, j = q.popleft()
                grid[i][j] = dist
                addN(i, j)
            
            dist += 1
        

            
        

                    

            







                    
            



        