class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = Counter('balloon')
        text_c  = Counter(text)
        
        min_times = len(text)
        
        for c in balloon:
            min_times = min(min_times, text_c.get(c, 0) // balloon[c])
        
        return min_times
        