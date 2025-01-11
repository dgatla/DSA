from typing import List


class Solution:
    """You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.

    Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').

    Return the final string after all such shifts to s are applied.
    """

    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        sweep = [0 for _ in range(len(s) + 1)]

        for shift in shifts:
            start, end, direction = shift

            sweep[start] += (2 * direction) - 1
            sweep[end + 1] -= (2 * direction) - 1

        ans = ['' for _ in range(len(s))]
        shift = 0
        for i, c in enumerate(s):
            shift += sweep[i]

            new_c = (ord(c) - 97 + shift) % 26 + 97

            ans[i] = chr(new_c)

        return ''.join(ans) 
            


