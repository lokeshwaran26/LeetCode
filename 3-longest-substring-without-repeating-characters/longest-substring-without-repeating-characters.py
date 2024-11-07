class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        l = 0
        while l <= len(s):
            var = ""
            r = l
            while r < len(s) and s[r] not in var: 
                    var+=s[r]
                    r+=1
            l+=1
            count = max(count, len(var))

        return count

