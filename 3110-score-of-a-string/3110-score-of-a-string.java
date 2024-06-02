class Solution {
    public int scoreOfString(String s) {
        
      int l = 0;
      int r = 1;
      int res = 0;
      while(r < s.length()){
        
        res+= Math.abs(((int) s.charAt(l)) - ((int) s.charAt(r)));
        l++;
        r++;
        
      }
      return res;
    }
}