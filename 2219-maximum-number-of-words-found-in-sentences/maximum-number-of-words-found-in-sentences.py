class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        word = []
        maxi = 0
        for  i in sentences:
            li = i.split()
            word.append(li)
        
        for i in word:
            maxi = max(len(i), maxi)

        return maxi


        


        