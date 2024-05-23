class Solution {
    public double findMaxAverage(int[] nums, int k) {
        
        double currSum = 0;
        for(int i=0;i<k;i++){
            currSum+= nums[i];
        }
        
        double max = currSum;
        
        for(int j=k;j<nums.length;j++){
            currSum += nums[j] - nums[j-k];
            
            max = Math.max(currSum, max);
        }
        return max / k;
    }
}