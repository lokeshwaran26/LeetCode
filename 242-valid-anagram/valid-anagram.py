class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        t1 = {}
        for i in s:
            if i not in s1:
                s1[i] = 1
            else:
                s1[i]+=1
        for i in t:
            if i not in t1:
                t1[i] = 1
            else:
                t1[i]+=1
        
        if s1 == t1:
            return True
        else:
            return False

        print(s1)
        print(t1)
        