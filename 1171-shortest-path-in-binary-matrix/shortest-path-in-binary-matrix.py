class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        if n == 1:
            return 1
        
        dirs = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
        queue = deque([(0, 0, 1)])
        grid[0][0] = -1
        
        while queue:
            i, j, steps = queue.popleft()
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 0:
                    if ni == n-1 and nj == n-1:
                        return steps + 1
                    queue.append((ni, nj, steps + 1))
                    grid[ni][nj] = -1 
        return -1