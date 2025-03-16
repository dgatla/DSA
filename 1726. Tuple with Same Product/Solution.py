from collections import defaultdict
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        mp = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                mp[nums[i] * nums[j]] += 1
        
        ans = 0
        
        for k, v in mp.items():
            total_pairs = (v * (v - 1)) // 2
            ans += (total_pairs  * 8)
        
        return ans