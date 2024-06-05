class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l = 0 
        r = len(height) - 1
        
        max_ = 0
        while(l < r):
            
            h = min(height[l], height[r])
            area = h * (r-l)
            max_ = max(max_, area)
            
            if(height[l] < height[r]):
                l+=1
            else:
                r-=1
        
        return max_
        