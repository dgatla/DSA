from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        s1, s2 = set(), set()
        ans = 0
        res = []
        for x, y in zip(A, B):
            if x == y:
                ans += 1
            else:
                if x in s2:
                    ans += 1
                s1.add(x)
                if y in s1:
                    ans += 1
                s2.add(y)
            
            res.append(ans)
        return ans