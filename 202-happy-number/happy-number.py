class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        def get_next(n):
            out = 0
            while n:
                digi = n % 10
                out += digi ** 2
                n = n // 10
            return out

        while n not in visit:
            visit.add(n)
            n = get_next(n)
            if n == 1:
                return True
        
        return False







        