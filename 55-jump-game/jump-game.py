class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif gas < n:
                gas = n
            gas-=1
        return True

            

            




        