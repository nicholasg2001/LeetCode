class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        sum_ = sum(nums)
        
        n = len(nums)

        sum_nums = (n*(n+1)) // 2

        
        return sum_nums - sum_

        