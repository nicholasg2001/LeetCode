class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        for num in nums[:k]:
            sum += num
        ans = sum
        i = k
        while i < len(nums):
            sum+= nums[i] - nums[i-k]
            ans = max(ans, sum)
            i += 1
        return ans / k
        