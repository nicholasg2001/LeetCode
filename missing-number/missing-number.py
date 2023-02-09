class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        inNums = set()
        for i in range(0, len(nums)+1):
            if i in nums:
                inNums.add(i)
            else:
                return i
        