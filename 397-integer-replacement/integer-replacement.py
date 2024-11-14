class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        while n > 1:
            if n % 2 == 0:
                n = n//2
            elif n == 3 or (n // 2) %2 == 0:
                n = n-1
            else:
                n = n+1
            count+=1
        return count
        