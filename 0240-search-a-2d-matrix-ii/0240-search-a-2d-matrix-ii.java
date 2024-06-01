class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        
        int rows = matrix.length;
        int cols = matrix[0].length;
        
        int row = rows-1;
        int col = 0;
        
        while(row >= 0 && col < cols){
            
            if(matrix[row][col] == target){
                return true;
            }
            else if(matrix[row][col] < target){
                col++;
            }
            else{
                row--;
            }
        }
        return false;
        
    }
}