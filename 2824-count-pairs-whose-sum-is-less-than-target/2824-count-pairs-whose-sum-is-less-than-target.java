class Solution {
    public int countPairs(List<Integer> nums, int target) {
        
        nums.sort(null);
        int l = 0;
        int r = nums.size() -1;
        int c = 0;
        while(l < r){
            if(nums.get(l) + nums.get(r) < target){
                c+= (r-l);
                l++;
            } else{
                r--;
            }
        }
        return c;
        
    }
}