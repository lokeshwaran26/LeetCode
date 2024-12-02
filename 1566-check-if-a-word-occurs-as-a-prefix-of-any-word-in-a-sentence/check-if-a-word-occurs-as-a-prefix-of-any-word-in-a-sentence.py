class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        pos = 0
        sen = sentence.split()
        for i in range(len(sen)):
            word = sen[i]
            n = ""
            if len(word) < len(searchWord):
                continue
            l = 0
            while l < len(searchWord):
                if word[l] == searchWord[l]:
                    n+=word[l]
                if n == searchWord:
                    pos = i+1
                    return pos
                l+=1
        return -1





        