class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = 0
        n2 = 0
        for char in num1:
           digit = ord(char) - ord('0')
           n1 = n1 * 10 + digit 
        for char in num2:
           digit = ord(char) - ord('0')
           n2 = n2 * 10 + digit 

        digit = n1*n2
        result = "%s" % digit
        return result
        



        