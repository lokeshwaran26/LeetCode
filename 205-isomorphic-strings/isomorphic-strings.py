class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_s = {}
        char_t = {}

        for i in range(len(s)):
            if s[i] not in char_s:
                char_s[s[i]] = i

            if t[i] not in char_t:
                char_t[t[i]] = i

            if char_s[s[i]] != char_t[t[i]]:
                return False

        return True

            

        