class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index_insert = len(nums)

        for i, val in enumerate(nums):
            if val == target:
                return i
            
            if val > target and index_insert == len(nums):
                index_insert = i
        
        return index_insert