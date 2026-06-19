from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        empty, fresh, rotten = 0, 1, 2
        q = deque()
        m, n = len(grid), len(grid[0])
        fresh_oranges = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == rotten:
                    q.append((i,j))
                elif grid[i][j] == fresh:
                    fresh_oranges += 1
        
        if fresh_oranges == 0:
            return 0
        
        minutes = -1
        while q:
            q_size = len(q)
            minutes += 1
            for _ in range(q_size):
                i, j = q.popleft()
                for r, c in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                    if 0<=r<m and 0<=c<n and grid[r][c] == fresh:
                        grid[r][c] = rotten
                        q.append((r,c))
                        fresh_oranges -= 1
        if fresh_oranges == 0:
            return minutes
        else:
            return -1

        