class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        ans = []
        
        if(len(original) == m*n):
            row = []
            for i in range(len(original)):
                row.append(original[i])
                if len(row) == n:
                    ans.append(row)
                    row = []
        return ans
            
            
        
        
        