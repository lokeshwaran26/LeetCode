class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        l = 0
        while l < len(arr):
            r = 0
            while r < len(arr):
                if l!=r and arr[l] == 2*arr[r]:
                    return True
                r+=1
            l+=1
        return False
        