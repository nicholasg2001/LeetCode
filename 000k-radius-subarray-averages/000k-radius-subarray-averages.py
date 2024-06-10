class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        """

        [7, 4, 3, 9, 1, 8, 5, 2, 6]


          0  1  2 3  4  5   6  7  8
        [-1,-1,-1,5, 4, 4, -1,-1,-1]

        """
        n = len(nums)
        res = [-1] * n
        left = 0
        sum_ = 0
        length = 2*k+1

        for r in range(n):
            sum_ += nums[r]

            if r - left + 1 == length:
                res[left+k] = sum_ // length

                sum_ -= nums[left]
                left+=1
        return res