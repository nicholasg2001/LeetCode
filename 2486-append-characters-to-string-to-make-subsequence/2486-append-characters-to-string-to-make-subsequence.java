class Solution {
    public int appendCharacters(String s, String t) {
        
        int p = 0;
        
        for(char c: s.toCharArray()){
            
            if(p == t.length()){
                break;
            }
            if(c == t.charAt(p)){
                p++;
            }
        }
        return(t.length() - p);
        
    }
}