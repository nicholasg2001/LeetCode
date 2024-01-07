class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        result = 0
        
        for i in range(n+1):
            result ^= i
            
        for num in nums:
            result ^= num
        
        return result
        