import math
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        dp = [[math.inf for _ in range(n)] for _ in range(m)]
        mp = {1: [0, 1], 2:[0,-1], 3:[1, 0], 4:[-1, 0]}
        def recurse(i, j , cost):

            if i < 0 or j < 0 or i >= m or j >= n: return math.inf

            if i == m - 1 and j == n- 1: return cost

            if dp[i][j] != math.inf:
                return dp[i][j]

            follow_i, follow_j = mp[grid[i][j]]

            best_cost = math.inf

            for k, v in mp.items():
                di, dj = mp[grid[i][j]]
                follow_i, follow_j = i + di, j + dj
                if k == grid[i][j]:
                    best_cost = min(best_cost, recurse(follow_i, follow_j, cost))
                else:
                    best_cost = min(best_cost, recurse(follow_i, follow_j, cost + 1))
                
            dp[i][j] = best_cost

            return best_cost

        return recurse(0, 0 , 0)


        