class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        originalX = x
        numReversed = 0
        
        while(originalX > 0):
            
            lastDigit = originalX % 10
            numReversed = (numReversed * 10) + lastDigit
            originalX//=10
        
        
        return numReversed == x
        