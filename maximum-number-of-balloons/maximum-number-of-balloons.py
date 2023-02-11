class Solution:
    def maxNumberOfBalloons(self, s: str) -> int:
        counts = defaultdict(int)
        ans = 0
        
        for c in s:
            counts[c]+=1
            if counts['b']>= 1 and counts['a'] >= 1 and counts['l'] >= 2 and counts['o'] >= 2 and counts['n'] >= 1:
                ans +=1
                counts['b']-=1
                counts['a']-=1
                counts['l']-=2
                counts['o']-=2
                counts['n']-=1
        return ans
        