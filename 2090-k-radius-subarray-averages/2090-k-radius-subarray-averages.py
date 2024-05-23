class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        
        res = [-1] * n
        
        if(k >= n / 2):
            return res
        
        max_ = len(nums) - k
        currSum = sum(nums[:2*k+1])
        res[k] = currSum // ((2*k) + 1)
        
        
        for i in range(k+1, max_):
            currSum += nums[i+k] - nums[i-k-1]
            print(currSum)
            res[i] = currSum // ((2*k) + 1)
        
        return res
            
            
            