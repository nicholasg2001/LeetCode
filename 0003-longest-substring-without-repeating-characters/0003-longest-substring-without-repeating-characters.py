class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counts = defaultdict(int)
        left = right = ans = 0;
        while(right < len(s)):
            counts[s[right]]+=1
            while(counts[s[right]]>1):
                counts[s[left]]-=1
                if counts[s[left]] == 0:
                    del counts[s[left]]
                left+=1
            ans = max(ans, right-left+1)
            right+=1
        return ans
            
        