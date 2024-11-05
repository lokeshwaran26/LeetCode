class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums[:] = sorted(set(nums))
        # return len(nums)
        l = 0
        r = 1
        while r < len(nums):
            if nums[r] != nums[l]:
                l+=1
                nums[l] = nums[r]
            r+=1
        return l+1



        