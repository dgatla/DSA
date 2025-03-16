from tracemalloc import start
from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        directions = ((0, -1), (0, 1), (1, 0), (-1, 0))

        def recursively_find(x , y, starting=False) -> int:
            if x < 0 or y < 0 or x >= m or y >= n or (grid[x][y] == 0 and starting):
                return 0

            if dp[x][y]: return dp[x][y]

            ans = grid[x][y]

            for dx, dy in directions:
                ans += recursively_find(x + dx, y + dy)
            
            dp[x][y] = ans
            return ans

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    ans = max(ans, recursively_find(i, j, True))
        
        return ans