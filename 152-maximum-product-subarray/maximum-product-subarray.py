class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        print(res,"\n")
        curMax, curMin = 1, 1

        for n in nums:
            tmp  = n * curMax
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            print(curMax)
            res = max(res, curMax)
        return res