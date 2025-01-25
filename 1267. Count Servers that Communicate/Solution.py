from re import L
from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ans = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        m, n = len(grid), len(grid[0])
        def dfs(x, y) -> int:
            if x < 0 or y < 0 or x == m or y == n:
                return -1
            
            if grid[x][y] == 0:
                return -1
            maxi = 1
            grid[x][y] = 0
            for direction in directions:
                next_x, next_y = x + direction[0], y + direction[1]
                res = dfs(next_x, next_y)
                if res != -1:
                    maxi += res
            return maxi

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i,j))
        
        return ans
                


        