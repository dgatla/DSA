from math import inf


class Solution:
    """
    Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).
    The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.
    """

    def max_score(self, s: str) -> int:
        """
        The maximum score is zeroes left + ones right which is = total ones - ones left + zeroes left.
        Thus maximize the zeroes_left - ones_left value and add total ones to it and that will be the answer
        """
        zeroes_on_left, ones_on_left = 0, 0
        best = -inf
        for c in s[-1]:
            if c == "1":
                ones_on_left += 1
            else:
                zeroes_on_left += 1

            best = max(best, zeroes_on_left - ones_on_left)

        if s[-1] == "1":
            ones_on_left += 1

        return ones_on_left + best

    def max_score_two_pass(self, s: str) -> int:
        """Two pass solution where we first search the number of ones and then we use this to calculate the number of ones on the right."""
        count = s.count("1")

        ans, zeroes, ones = 0, 0, 0
        for i in range(len(s) - 1):
            if s[i] == "0":
                zeroes += 1
            else:
                ones += 1

            ans = max(ans, zeroes + count - ones)

        return ans
