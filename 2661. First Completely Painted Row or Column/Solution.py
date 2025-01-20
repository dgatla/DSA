from collections import defaultdict
from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        pos_map = {}

        for i, row in enumerate(mat):
            for j, col in enumerate(row):
                pos_map[col] = (i, j)
            
        processed_arr = [pos_map[i] for i in arr]

        m, n = len(mat), len(mat[0])
        rows, cols = defaultdict(list), defaultdict(list)

        for index,(i, j) in enumerate(processed_arr):
            rows[i].append(j)
            cols[j].append(i)
            if len(rows[i]) == n or len(cols[j]) == m:
                return index
        
        return -1
