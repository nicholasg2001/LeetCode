class Solution {
    public String[] divideString(String s, int k, char fill) {
    
        if(s.length()%k>0){
            for(int i=0; i<s.length()%k; i++){
                s+=fill;
            }
        }

        String[] res = new String[s.length()/k];  
        int index = 0; 
        for(int i = 0; i < s.length(); i+=k){
            res[index] = s.substring(i, i+k); 
            index++;
        }
        return res;
    }
}