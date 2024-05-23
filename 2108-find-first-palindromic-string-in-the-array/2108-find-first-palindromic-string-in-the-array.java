class Solution {
    
    public Boolean isPalindrome(String word){
        int l = 0;
        int r = word.length() - 1;
        
        while(l < r){
            if(word.charAt(l) != word.charAt(r)){
                return false;
            }
            l++;
            r--;
        }
        return true;
        
    }
    
    
    public String firstPalindrome(String[] words) {
        
        for(String word: words){
            if(isPalindrome(word)){
                return word;
            }
        }
        return "";
        
    }
}