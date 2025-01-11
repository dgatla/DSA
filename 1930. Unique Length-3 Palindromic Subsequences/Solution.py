from typing import Counter


class Solution:
    """Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

    Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

    A palindrome is a string that reads the same forwards and backwards.

    A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde".
    """

    def count_palindrome_subsequence(self, s:str)->int:
        mp = Counter(s)

        ans = 0
        seen = set()
        for c in s:
            if c in seen:
                mp[c] -= 1
                continue
            
            if mp[c] == 0:
                del mp[c]
            
            if mp[c] >= 2:
                ans += len(mp)
                ans += 1 if mp[c] > 2 else 0
            mp[c] -=1
        return ans
