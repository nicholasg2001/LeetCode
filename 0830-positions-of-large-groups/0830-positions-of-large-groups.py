class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        
        
        n = len(s)
        res = []

        if(n < 3):
            return res
        
        i=0
        for r in range(n):
            if r == n-1 or s[r] != s[r+1]:
                if r-i+1 >= 3:
                    res.append([i, r])
                
                i=r+1
        
        return res