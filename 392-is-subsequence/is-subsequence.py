class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True 
        sums = 0
        l = 0
        for r in range(len(t)):
            if l < len(s) and s[l] == t[r]:
                sums+=1
                l+=1
        return sums == len(s)

        