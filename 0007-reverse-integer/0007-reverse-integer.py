class Solution:
    def reverse(self, x: int) -> int:
        max_int = 2 ** 31 - 1
        min_int = -2 ** 31

        reverse = 0
        while x != 0:
            if reverse > max_int / 10 or reverse < min_int / 10:
                return 0 
            digit = x % 10 if x > 0 else x % - 10
            reverse = reverse * 10 + digit
            x = math.trunc(x / 10)
        
        return reverse
