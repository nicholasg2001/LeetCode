class Solution:
    def scoreOfString(self, s: str) -> int:
        
        l = 0
        i = 1
        res = 0

        while(i < len(s)):
          res+= abs((ord(s[l]) - ord(s[i])))
          print(s[l])
          print(s[i])
          l+=1
          i+=1
          
        
        return res
          