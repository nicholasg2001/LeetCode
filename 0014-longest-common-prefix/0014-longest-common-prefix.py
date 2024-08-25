class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""
        
        shortest = min(strs, key=len)
        ans = ""

        for i, char in enumerate(shortest):
            for other in strs:
                if other[i] != char:
                    return ans
            
            ans+=char
        
        return ans
        