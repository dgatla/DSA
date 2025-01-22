from math import inf
from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        l = len(grid[0])
        suffix = [0 for _ in range(l)]
        suffix[-1] = grid[1][-1]
        for i in range(l - 2, -1, -1):
            suffix[i] = grid[1][i] + suffix[i+1]
        

        bot_a_turning_down_sum = -1
        bot_a_best = -inf
        bot_a_prefix = 0
        bot_a_turning_down = -1

        for i in range(l):
            bot_a_prefix += grid[0][i]
            total_score = bot_a_prefix + suffix[i]
            if bot_a_best < total_score:
                bot_a_best = total_score
                bot_a_turning_down = i
                bot_a_turning_down_sum = bot_a_prefix
        print(bot_a_turning_down, bot_a_best, bot_a_prefix, bot_a_turning_down_sum)
        print(suffix)
        return max((bot_a_prefix - bot_a_turning_down_sum), (suffix[0] - suffix[bot_a_turning_down - 1]))


        