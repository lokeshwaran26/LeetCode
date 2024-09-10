from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_c  = Counter(s)

        long_pal = 0
        odd_c = False

        for count in char_c.values():
            if count % 2 == 0:
                long_pal += count
            else:
                odd_c = True
                long_pal += count -1
        
        if odd_c:
            long_pal+=1
        
        return long_pal
        