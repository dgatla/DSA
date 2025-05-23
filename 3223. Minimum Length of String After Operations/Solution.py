from collections import Counter


class Solution:
    """
        You are given a string s.

    You can perform the following process on s any number of times:

    Choose an index i in the string such that there is at least one character to the left of index i that is equal to s[i], and at least one character to the right that is also equal to s[i].
    Delete the closest character to the left of index i that is equal to s[i].
    Delete the closest character to the right of index i that is equal to s[i].
    Return the minimum length of the final string s that you can achieve.
    """

    def minimumLength(self, s: str) -> int:
        ans = 0
        count = Counter(s)
        for v in count.values():
            if v % 2 == 0:
                ans += 2
            else:
                ans += 1
        return ans
