class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for idx, num in enumerate(nums):

            compliment = target - num
            if compliment in seen:
                return [idx, seen[compliment]]
            seen[num] = idx
            
