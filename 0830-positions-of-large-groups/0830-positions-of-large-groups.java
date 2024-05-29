class Solution {
    public List<List<Integer>> largeGroupPositions(String s) {
        
        
        List<List<Integer>> res = new ArrayList<>();
        
        int i = 0;
        
        for(int r=0;r<s.length();r++){
            if(r == s.length()-1 || s.charAt(r) != s.charAt(r+1)){
                if(r-i+1 >= 3){
                    res.add(List.of(i, r));
                }
                
                i = r+1;
            }
        }
        return res;
    }
}