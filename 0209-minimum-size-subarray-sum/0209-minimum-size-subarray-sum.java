class Solution {
    public int minSubArrayLen(int target, int[] nums) {

        int left = 0;
        int ans = Integer.MAX_VALUE;
        int total = 0;
        for(int right = 0; right < nums.length; right++){
            total = total + nums[right];

            while(total >= target) {

                ans = Math.min(ans, right-left+1);
                total = total - nums[left];
                left++;
            }
        }
        return (ans == Integer.MAX_VALUE) ? 0 : ans;
    }
}