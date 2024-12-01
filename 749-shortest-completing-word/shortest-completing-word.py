class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        count = {}
        shortest_word = None
        shortest_length = float("inf") #Assigning the infinity limit

        # 1. Counting the license plate without  
        for char in licensePlate:
            if char.isalpha():
                char = char.lower()
                count[char] =count.get(char,0)+1

        # 2. Counting the characters in word from words 
        for word in words:
            word_count ={}
            for char in word:
                word_count[char] = word_count.get(char,0)+1
            is_Valid = True

        # 3. Checking if there is any letter not there 
            for char,freq in count.items():
                if word_count.get(char,0) < freq:
                    is_Valid =False
                    break
            
        # 4. If it valid then finding shortest word
            if is_Valid:
                if len(word)<shortest_length:
                    shortest_length = len(word)
                    shortest_word = word
        
        return shortest_word