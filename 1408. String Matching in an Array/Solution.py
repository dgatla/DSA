from typing import List


class Solution:
    """
    Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.

    A substring is a contiguous sequence of characters within a string
    """

    def string_matching(self, words:List[str]) -> List[str]:
        ans = []

        for i, c in enumerate(words):
            for j, d in enumerate(words):
                if i == j: continue
                if c in d:
                    ans.append(c)
                    break
            
        return ans
