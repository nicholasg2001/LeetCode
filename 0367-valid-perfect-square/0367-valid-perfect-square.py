class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = num
        
        while(l <= r):
            
            m = l + ((r - l) // 2)
            
            if m**2 > num:
                r = m - 1
            elif m**2 < num:
                l = m + 1
            else:
                return True
        
        return False
        