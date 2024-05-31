class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        map_ = {}
        
        for num in nums1:
            
            map_[num] = map_.get(num, 0) + 1
        
        
        res = []
        for num in nums2:
            if num in map_:
                res.append(num)
                del map_[num]
        
        return res
        