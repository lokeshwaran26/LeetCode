class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        out = []
        for l in range(len(nums) - 2):
            if l > 0 and nums[l] == nums[l-1]:
                continue
            m = l+1
            r = len(nums) -1
            while m<r:
                total = nums[l] + nums[m] + nums[r]
                if total > 0:
                    r-=1
                elif total < 0:
                    m+=1
                else:
                    li = [nums[l],nums[m],nums[r]]
                    out.append(li)
                    m+=1
                    while nums[m] == nums[m -1] and m < r:
                        m+=1
                
        return out
        




        

        