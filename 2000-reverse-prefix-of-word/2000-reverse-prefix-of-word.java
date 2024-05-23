class Solution {
    public String reversePrefix(String word, char ch) {
        
        for(int i =0;i<word.length();i++){
            
            if(word.charAt(i) == ch){
                int s = i+1;
                StringBuilder sb = new StringBuilder();
                while (i >= 0){
                    sb.append(word.charAt(i));
                    i--;
                }
                while(s < word.length()){
                    sb.append(word.charAt(s));
                    s++;
                }
                return sb.toString();
            }
        }
        return word;
    }
}