class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        
        for i in range(len(nums)):
            num = nums[i]
            compliment = target - num
            if compliment in dict:
                return [i, dict[compliment]]
            dict[num]=i
        return [-1, -1]

        