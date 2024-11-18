class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        res = []
        while l < len(nums):
            r = l+1
            while r < len(nums):
                if nums[l] + nums[r] == target:
                    return [l, r]
                r+=1
            l+=1
        