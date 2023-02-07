class Solution {
    public int minStartValue(int[] nums) {
        int total = 0;
        int minVal = 0;
        for(int i=0;i<nums.length;i++){
            total+=nums[i];
            if (total < minVal){
                minVal = total;
            }
        }
        total = 1 - minVal;
        return total;
    }
}