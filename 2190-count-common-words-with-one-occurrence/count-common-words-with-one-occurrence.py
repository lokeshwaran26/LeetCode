class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count=0

        for i in words1:
            if words1.count(i)==1 and words2.count(i)==1:
                count=count+1

        return count