class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        pref, cnt = [0], 0
        for a, b in pairwise(nums):
            if (a + b) % 2 == 1:
                cnt += 1
            pref.append(cnt)
        ans = []
        for a, b in queries:
            ans.append(pref[b]-pref[a] == b-a)
        return ans