class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        column = 0
        row = len(matrix) - 1
        
        #number at matrix[row][col] smaller than target, then go to next row up
        #if the number 
        
        while(row >= 0 and column < len(matrix[0])):
            
            if(matrix[row][column] < target):
                column+=1
            
            elif(matrix[row][column] > target):
                row-=1
            else:
                return True
        
        return False