class Solution {
    public int majorityElement(int[] nums) {
        
        int res = 0;
        int count = 0;
        
        for(int n : nums){
            
            if(count == 0){
                res = n;
            }
            
            if(res == n){
                count+=1;
            } else {
                count-=1;
            }
        }
        return res;
    }
}