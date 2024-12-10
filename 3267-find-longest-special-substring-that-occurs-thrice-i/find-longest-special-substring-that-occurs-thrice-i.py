class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        mp = {}
        for i in range(n):
            for j in range(i, n):
                substring = s[i:j + 1]
                unique_chars = set(substring)
                if len(unique_chars) == 1:
                    mp[substring] = mp.get(substring, 0) + 1

        maxi = -1
        for key, value in mp.items():
            if value >= 3:
                maxi = max(maxi, len(key))

        return maxi