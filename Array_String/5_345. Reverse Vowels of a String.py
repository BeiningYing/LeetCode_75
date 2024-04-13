# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

class Solution:
    def reverseVowels(self, s: str) -> str:
        import re
        a = re.findall(r"[aeiouAEIOU]", s)
        ans = ""
        for i in s:
            if i not in "aeiouAEIOU":
                ans += i
            else:
                ans += a.pop()
        return ans