class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = {}
        maxi = 0
        for num in nums:
            if num in elements:
                elements[num]+=1
            else:
                elements[num] = 1
        
        for num in nums:
            if elements[num] > len(nums) // 2:
                return num
                

        
        