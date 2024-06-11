class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
      
      zero = 0
      one = 0 
      res = 0
      
      diff_index = {} # count[1] - count[0] -> index
      
      for i, n in enumerate(nums):
        if n == 0:
          zero +=1
        else:
          one +=1
        
        if one - zero not in diff_index:
          diff_index[one - zero] = i
        
        if one == zero:
          res = one + zero
      
        else:
          idx = diff_index[one - zero]
          res = max(res, i - idx)
      
      return res
        