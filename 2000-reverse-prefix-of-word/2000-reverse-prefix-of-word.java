class Solution {
    public String reversePrefix(String word, char ch) {
        
        int check = word.indexOf(ch) ;
        
        
        if(check == -1){
            return word;
        } else {
            int s = check+1;
            StringBuilder sb = new StringBuilder();
            while (check >= 0){
                sb.append(word.charAt(check));
                check--;
            }
            while(s < word.length()){
                sb.append(word.charAt(s));
                s++;
            }
            return sb.toString();
        }
    }
}