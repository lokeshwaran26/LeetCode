class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n == 1:
            return nums[0]

        
        temp = 1
        while temp < n:
            if  nums[temp-1] != nums[temp]:
                return nums[temp-1]
            temp += 2    
        return nums[temp-1] 
        