class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        total_elements = len(nums)
        removed_elements = nums.count(val)

        for i in range(removed_elements):
            nums.remove(val)
        
        print(nums)
        
        elements_after_removal = len(nums)
        k = total_elements - removed_elements
        return k
        