class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiopQWERTYUIOP"
        row2 = "asdfghjklASDFGHJKL"
        row3 = "zxcvbnmZXCVBNM"
        out = []

        for word in words:
            row = ""
            Find = True
            if word[0] in row1:
                row = row1
            elif word[0] in row2:
                row = row2
            else:
                row = row3
            for i in range(1,len(word)):
                if word[i] not in row:
                    Find = False
                    break
            if Find : out.append(word)
        
        return out


        