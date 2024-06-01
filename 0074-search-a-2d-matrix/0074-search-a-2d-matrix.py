class Solution:
    
    def binarySearch(self, nums: List[int], target: int) -> bool:
        
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            
            mid = (low + high) // 2
            
            if(nums[mid] < target):
                low = mid + 1
            elif(nums[mid] > target):
                high = mid - 1
            else:
                return True
        return False
        
        
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        top = 0
        bot = rows - 1
        
        while top <= bot:
            row = (top + bot) // 2
            if(matrix[row][-1] < target):
                top = row + 1
            
            elif(matrix[row][0] > target):
                bot = row - 1
                
            else:
                break
        
        if not (top <= bot):
            return False
        else:
            return self.binarySearch(matrix[(top+bot) // 2], target)
                
        
        
            
        