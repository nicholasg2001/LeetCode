class Solution:
    
    def isPalindrome(self, word: str) -> bool:
        
        l = 0
        r = len(word) - 1
        
        while l < r:
            if word[l] != word[r]:
                return False
            l+=1
            r-=1
        return True
        
        
        
    
    def firstPalindrome(self, words: List[str]) -> str:
            
            for word in words:
                if self.isPalindrome(word):
                    return word
            
            return ""