# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        lens1, lens2 = len(str1), len(str2)

        # 字符串长度
        def divide(l):
            # 排除不能整除的情况
            if lens1%l or lens2%l:
                return False

            f1, f2 = lens1//l, lens2//l
            if f1 * str1[:l] == str1 and f2 * str1[:l]== str2:
                return True
            else: 
                return False
            # 或：return f1*str1[:l]==str1 and f2 * str1[:l]

        for l in range(min(lens1,lens2), 0, -1):
            if divide(l):
                return str1[:l]

        return ""