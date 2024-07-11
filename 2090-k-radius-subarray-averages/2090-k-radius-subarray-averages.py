class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        window_size = (2*k) + 1
        if n < window_size:
            return [-1] * n
        elif k == 0:
            return nums

        res = [-1] * n
        sum_ = 0
        for i in range(0, 2*k+1):
            sum_ += nums[i]
        res[k] = sum_ // window_size

        for i in range(k+1, n-k):
            sum_ -= nums[i-k-1]
            sum_ += nums[i+k]
            res[i] = sum_ // window_size

        return res