class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        maxC = max(candies)
        
        for kid in candies:
            if kid + extraCandies >= maxC:
                res.append(True)
            else:
                res.append(False)
        
        return res
        
                
        