class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        keys = {"type" : 0, "color" : 1, "name" : 2}
        keyval = 0
        out = 0
        for key, value in keys.items():
            if key == ruleKey:
                keyval = value
        # print(keyval)
        for i in range(len(items)):
            if items[i][keyval] == ruleValue:
                out+=1
        return out

        