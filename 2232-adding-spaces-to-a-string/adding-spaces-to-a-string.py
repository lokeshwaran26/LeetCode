class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        out = ""
        n = 0
        for i in range(len(s)):
            if n< len(spaces) and i == spaces[n]:
                out+=" "
                n+=1
            
            out+=s[i] 
        return out
