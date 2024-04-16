# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(t)
        # 不需要转换成list，string可以直接使用[]
        # ls = list(s)
        # lt = list(t)
        j = 0
        for i in range(n):
            if j < len(s):
                if s[j] == t[i]:
                    j += 1
        # Include: s = null
        if j == len(s):
            return True
        else:
            return False

            
            