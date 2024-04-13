# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        i = j = 0
        ans = ""
        while i < m or j < n:
            if i < m:
                ans += word1[i]
                i += 1
            if j < n:
                ans += word2[j]
                j += 1
        return ans                


        # ans = list()
        # while i < m or j < n:
        #     if i < m:
        #         ans.append(word1[i])
        #         i += 1
        #     if j < n:
        #         ans.append(word2[j])
        #         j += 1
        # return "".join(ans)
