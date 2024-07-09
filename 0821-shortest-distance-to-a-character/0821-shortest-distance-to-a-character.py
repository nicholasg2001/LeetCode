class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        
        idx_of_c = []
        res = []

        for i, char in enumerate(s):
            if char == c:
                idx_of_c.append(i)
        
        for i in range(len(s)):

            min_distance = min(abs(i - idx) for idx in idx_of_c)
            result.append(min_distance)
        
        return result
