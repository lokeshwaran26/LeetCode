class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sen = sentence.split()
        dictionary.sort()
        for word in dictionary:
            for i in range(len(sen)):
                if sen[i].startswith(word):
                    sen[i] = word
                    
        return " ".join(sen)

        