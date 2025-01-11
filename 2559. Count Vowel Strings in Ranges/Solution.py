from typing import List


class Solution:
    """You are given a 0-indexed array of strings words and a 2D array of integers queries.

    Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.

    Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

    Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.
    """

    def vowel_strings(words: List[str], queries: List[List[int]]) -> List[int]:
        pre_compute = [0 for _ in range(len(words))]
        vowels = {"a", "e", "i", "o", "u"}
        pre_compute[0] = 1 if words[0][0] in vowels and words[0][-1] in vowels else 0

        for i in range(1, len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                pre_compute[i] = pre_compute[i - 1] + 1
            else:
                pre_compute[i] = pre_compute[i - 1]
        res = [0 for _ in range(len(queries))]
        for i, query in enumerate(queries):
            start, end = query
            res[i] = (
                pre_compute[end] - pre_compute[start - 1]
                if start != 0
                else pre_compute[end]
            )

        return res
