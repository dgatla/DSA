from collections import defaultdict, deque
import heapq
from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sorted_nums = sorted(nums)

        numbers_mapped_to_group = {sorted_nums[0] : 0}

        groups = defaultdict(deque)

        current_group = 0
        groups[0].append(sorted_nums[0])

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] - sorted_nums[i - 1] > limit:
                current_group += 1
            numbers_mapped_to_group[sorted_nums[i]] = current_group
            groups[current_group].append(sorted_nums[i])

        for i in range(len(nums)):
            number_group = numbers_mapped_to_group[nums[i]]
            best_answer_here = groups[number_group].popleft()
            nums[i] = best_answer_here

        return nums        
