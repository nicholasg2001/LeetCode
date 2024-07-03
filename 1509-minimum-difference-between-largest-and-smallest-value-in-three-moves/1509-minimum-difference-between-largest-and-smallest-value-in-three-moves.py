class Solution:
    def shift(self, a: List[int], start: int) -> None:
        last = a[-1]
        for j in range(len(a) - 1, start, -1):
            a[j] = a[j - 1]
        if len(a) < 4:
            a.append(last)
    
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        min4 = [float('inf')] * 4
        max4 = [float('-inf')] * 4
        
        for num in nums:
            added = False
            for j in range(4):
                if num < min4[j]:
                    self.shift(min4, j)
                    min4[j] = num
                    added = True
                    break
            if not added and min4[-1] == float('inf'):
                min4[-1] = num
        
        for num in nums:
            added = False
            for j in range(4):
                if num > max4[j]:
                    self.shift(max4, j)
                    max4[j] = num
                    added = True
                    break
            if not added and max4[-1] == float('-inf'):
                max4[-1] = num
        
        ans = max4[0] - min4[0]
        for i in range(4):
            ans = min(ans, max4[3 - i] - min4[i])
        
        return ans