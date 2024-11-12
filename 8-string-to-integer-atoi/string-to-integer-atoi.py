class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        l = 0
        value = 0
        sign = 1
        if s[0] == '-':
            sign = -1
            l+=1
        elif s[0] == '+':
            l+=1

        while l < len(s) and s[l].isdigit():
            value = value * 10 + int(s[l])
            l+=1
        
        value = sign*value
        int_min, int_max = -2**31, 2**31 - 1
        if value < int_min:
            return int_min
        if value > int_max:
            return int_max

        return value




        
        