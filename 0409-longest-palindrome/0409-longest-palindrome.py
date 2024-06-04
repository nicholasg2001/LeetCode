class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        if len(s) == 1:
            return 1
        
        
        counts = {}
        lock = False
        res = 0
        for c in s:
            counts[c] = counts.get(c, 0) + 1
            if counts[c] % 2 == 0:
                res+=2
        
        for c in counts.values():
            if c % 2:
                res+=1
                break
            
        return res
        
        