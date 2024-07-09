class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.isPalindrome(s, 0, len(s)-1, 1)
    

    def isPalindrome(self, s: str, left: int, right: int, skips: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                if skips == 0:
                    return False
                return (self.isPalindrome(s, left+1, right, skips-1) or self.isPalindrome(s, left, right-1, skips-1))
                
            left+=1
            right-=1
        return True
        