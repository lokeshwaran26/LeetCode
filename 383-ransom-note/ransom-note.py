class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        for i in magazine:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        
        for char in ransomNote:
            if char not in count or count[char] == 0:
                return False
            
            count[char] -= 1

        return True
        




        
        