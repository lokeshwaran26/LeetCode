class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return n * [0]

        ext_code = code * 2
        
        if k > 0:
            return [ sum(ext_code[i+1: i+1+k]) for i in range(n)]
        if k < 0:
            k = abs(k)
            return [ sum(ext_code[i+ n -k: i+n]) for i in range(n)]
            


       
        