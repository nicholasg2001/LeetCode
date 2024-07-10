class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1

        rows = 0 
        cols = len(matrix[0]) - 1
        while(low <= high):
            
            mid = (low + high) // 2

            if matrix[mid][0] > target:
                high = mid - 1
            elif matrix[mid][-1] < target:
                low = mid + 1
            else:
                return self.binarySearch(matrix[mid], target)

        return False


    def binarySearch(self, nums: List[int], target: int) -> bool:

        low = 0
        high = len(nums) - 1
        while(low <= high):
            
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False