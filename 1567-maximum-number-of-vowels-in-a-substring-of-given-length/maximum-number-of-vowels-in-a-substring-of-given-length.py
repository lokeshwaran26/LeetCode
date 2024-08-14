class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        currentVowelsCount = 0

        for char in s[:k]:
            if char in vowels:
                currentVowelsCount += 1
        
        maxVowelsCount = currentVowelsCount

        i = 0
        
        while i < (len(s) - k):
            currentVowelsCount = currentVowelsCount - (s[i] in vowels) + (s[i + k] in vowels)
            maxVowelsCount = max(currentVowelsCount, maxVowelsCount)
            i += 1
        
        return maxVowelsCount