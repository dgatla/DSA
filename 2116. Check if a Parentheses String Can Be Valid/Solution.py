class Solution:
    """A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

    It is ().
    It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
    It can be written as (A), where A is a valid parentheses string.
    You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,

    If locked[i] is '1', you cannot change s[i].
    But if locked[i] is '0', you can change s[i] to either '(' or ')'.
    Return true if you can make s a valid parentheses string. Otherwise, return false.
    """

    def can_be_valid(self, s: str, locked: str):

        length = len(s)

        opening_brackets, closing_brackets, flexible_chars = 0, 0, 0

        for i,c in enumerate(s):
            if locked[i] == '0':
                flexible_chars += 1
            elif c == '(':
                opening_brackets += 1
            else:
                closing_brackets += 1
            
            if flexible_chars + opening_brackets - closing_brackets < 0:
                return False
        
        opening_brackets, closing_brackets, flexible_chars = 0, 0, 0
        
        for i, c in enumerate(s[::-1]):
            if locked[length - i - 1] == '0':
                flexible_chars += 1
            elif c == '(':
                opening_brackets += 1
            else:
                closing_brackets += 1
            
            if flexible_chars + closing_brackets - opening_brackets < 0:
                return False
        
        return True
