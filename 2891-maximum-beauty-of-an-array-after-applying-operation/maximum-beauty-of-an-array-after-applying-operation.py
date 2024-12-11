class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        for num in nums:
            if num - nums[left] > 2*k:
                left+=1
        return len(nums) - left



        