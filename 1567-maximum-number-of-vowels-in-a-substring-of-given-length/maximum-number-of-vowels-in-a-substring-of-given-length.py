class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        max_vowels = 0
        current_vowels = 0
        
        # Count vowels in the first window
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1
        max_vowels = current_vowels
        
        # Slide the window over the rest of the string
        for i in range(k, len(s)):
            # Remove the effect of the character that is sliding out of the window
            if s[i - k] in vowels:
                current_vowels -= 1
            # Add the effect of the character that is sliding into the window
            if s[i] in vowels:
                current_vowels += 1
            # Update the maximum number of vowels found
            max_vowels = max(max_vowels, current_vowels)
        
        return max_vowels
