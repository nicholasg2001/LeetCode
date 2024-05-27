class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        count = 0
        
        for cell in grid:
            for num in cell:
                if num < 0:
                    count+=1
        
        return count
                    
        