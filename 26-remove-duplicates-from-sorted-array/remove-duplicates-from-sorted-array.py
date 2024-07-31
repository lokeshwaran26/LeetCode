class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        nums[:] = sorted(set(nums))
        print(nums)
        return len(nums)

        # nums[:] = sorted(set(nums))       [1,1,2]
                                            #[1,2]
        # return len(nums)
        