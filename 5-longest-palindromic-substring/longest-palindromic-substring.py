class Solution:
    def longestPalindrome(self, s: str) -> str:
        sub_str = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if sub == sub[::-1]:
                    if len(sub) > len(sub_str):
                        sub_str = sub
        return sub_str
        