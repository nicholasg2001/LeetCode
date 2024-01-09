class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if (nums[index] < 0):
                res.append(index + 1)
            nums[index] = -1*nums[index]
            
        
        
        
        
        return res