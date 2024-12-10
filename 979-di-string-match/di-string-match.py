class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low, high = 0, len(s)
        prem = []
        for i in s:
            if i == "I":
                prem.append(low)
                low+=1
            elif i == "D":
                prem.append(high)
                high-=1

        prem.append(low)
        return prem
        