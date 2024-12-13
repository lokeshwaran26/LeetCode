class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        ord = list(range(n))
        
        ord.sort(key=lambda x: (nums[x], x))  # Sort indices by value and then by index
        # ord[:] = sorted(ord)
        
        m = [False] * n  
        score = 0
        
        for x in ord:
            if m[x]: continue 
            score += nums[x]  
            m[x] = True  
            if x > 0: m[x - 1] = True  
            if x + 1 < n: m[x + 1] = True  
        
        return score