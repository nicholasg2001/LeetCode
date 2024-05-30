class Solution {
    public int majorityElement(int[] nums) {
        
        Arrays.sort(nums);
        
        return nums[Math.floorDiv(nums.length, 2)];
    }
}