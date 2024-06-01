class Solution {
    
    public boolean binarySearch(int[] nums, int target){
        
        int low = 0;
        int high = nums.length - 1;
        
        while(low <= high){
            
            int mid = low + (high - low) / 2;
            
            if(nums[mid] < target){
                low = mid + 1;
            }
            else if(nums[mid] > target){
                high = mid - 1;
            }
            else {
                return true;
            }
        }
        return false;
    }
    
    public boolean searchMatrix(int[][] matrix, int target) {
        
        int rows = matrix.length;
        int cols = matrix[0].length;
        
        int top = 0;
        int bot = rows - 1;
        
        while(top <= bot){
            
            int row = Math.floorDiv((top+bot), 2);
            
            if(matrix[row][matrix[row].length - 1] < target){
                top = row + 1;
            }
            else if(matrix[row][0] > target){
                bot = row - 1;
            }
            else{
                break;
            }
        }
        if(!(top <= bot)){
            return false;
        }
        else{
            return binarySearch(matrix[Math.floorDiv((top+bot), 2)], target);
        }
        
    }
}