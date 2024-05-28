class Solution {
    public int mySqrt(int x) {
        
        int left = 0;
        int right = x;
        int mid;
        int res = 0;
        
        while(left <= right){
            
            mid = left + Math.floorDiv((right - left), 2);
            
            if(Math.pow(mid, 2) > x){
                right = mid -1;
            }
            else if(Math.pow(mid, 2) < x){
                left = mid + 1;
                res = mid;
            } else{
                return mid;
            }
        }
        return res;
    }
}