class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        words = {}
        out = []
        for i in range(len(list1)):
           for j in range(len(list2)):
                
               
                if list1[i] == list2[j] and list[i] not in words:
                    val = i + j
                    words[list1[i]] = val
                elif list1[i] == list2[j]:
                    val = i + j
                    words[list1[i]] = val
        mini = min(words.values())
        print(words)
        for key, value in words.items():
            if value == mini:
                out.append(key)
        return out


        
                    

        