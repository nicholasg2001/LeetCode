class Solution {
    
    public int sumArr(int[] account){
        
        int sum = 0;
        for(int i=0;i<account.length;i++){
            sum+=account[i];
        }
        return sum;
    }
    
    public int maximumWealth(int[][] accounts) {
        
        int max = 0;
        int sum = 0;
        
        for(int i=0;i<accounts.length;i++){
            sum = sumArr(accounts[i]);
            if(sum > max){
                max = sum;
            }
            sum = 0;   
        }
        return max;
    }
}