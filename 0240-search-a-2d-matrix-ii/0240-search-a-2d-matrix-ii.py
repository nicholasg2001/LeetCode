class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        rows = len(matrix)
        cols = len(matrix[0])

        row = rows-1
        col = 0

        while(row >= 0 and col < cols):

            if(matrix[row][col] < target):
                col+=1
            elif(matrix[row][col] > target):
                row-=1
            else:
                return True
        
        return False
