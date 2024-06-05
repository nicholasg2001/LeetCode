class Solution {
    public int maxArea(int[] height) {
        
        
        int l = 0;
        int r = height.length - 1;
        int max_ = 0;
        while(l < r){
            
            int h = Math.min(height[l], height[r]);
            int area = h * (r - l);
            max_ = Math.max(max_, area);
            
            if(height[l] < height[r]){
                l++;
            } else {
                r--;
            }
        }
        return max_;
    }
}