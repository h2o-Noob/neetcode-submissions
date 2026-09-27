class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        visited = set()
        rows, cols = len(grid), len(grid[0])
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        count = 0

        q = deque()

        def addN(i, j):
            for di, dj in direction:
                ni, nj = di + i, dj + j

                if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1 and (ni, nj) not in visited:
                    q.append([ni, nj])
                    visited.add((ni, nj))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append([i, j])
        
        while q:

            for k in range(len(q)):
                i, j = q.popleft()
                grid[i][j] = 2
                addN(i, j)
            if q:
                count += 1
            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        
        return count
        