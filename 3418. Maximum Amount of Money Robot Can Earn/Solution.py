from math import inf
from typing import List


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:

        m, n = len(coins), len(coins[0])

        dp = [[[-inf, -inf, -inf] for _ in range(n)] for _ in range(m)]

        def recurse(row, col, defence):

            if row == m - 1 and col == n - 1:
                if coins[row][col] < 0:
                    return coins[row][col] if defence == 0 else 0

                else:
                    return coins[row][col]
            
            if row >= m or col >= n or row < 0 or col < 0:
                return -inf

            if dp[row][col][defence] != -inf:
                return dp[row][col][defence]

            right_defence, down_defence = -inf, -inf
            right = recurse(row, col + 1, defence) + coins[row][col]
            if coins[row][col] < 0 and defence > 0:
                right_defence = recurse(row, col + 1, defence - 1)
            down = recurse(row + 1, col, defence) + coins[row][col]
            if coins[row][col] < 0 and defence > 0:
                down_defence = recurse(row + 1, col, defence - 1)
            
            best = max([right, right_defence, down, down_defence])

            dp[row][col][defence] = best

            return dp[row][col][defence]

        return recurse(0,0, 2)
            


