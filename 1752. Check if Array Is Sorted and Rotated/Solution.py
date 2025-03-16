from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        flag = False

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if flag:
                    return False
                flag = True
        return nums[-1] <= nums[0] if flag else True
