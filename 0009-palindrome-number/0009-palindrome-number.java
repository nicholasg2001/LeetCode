class Solution {
    public boolean isPalindrome(int x) {
        
        
        if(x < 0){
            return false;
        }
        
        int numReversed = 0;
        int originalX = x;
        int lastDigit;
        while(originalX > 0){
            
            lastDigit = originalX % 10;
            numReversed = (numReversed * 10) + lastDigit;
            originalX = Math.floorDiv(originalX, 10);
        }
        return x == numReversed;
    }
}