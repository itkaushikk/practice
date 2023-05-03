class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        output = []
        
        new_nums = []
        for val in nums1:
            if val in nums2:
                continue
            if val not in new_nums:
                new_nums.append(val)
        output.append(new_nums)

        new_nums = []
        for val in nums2:
            if val in nums1:
                continue
            if val not in new_nums:
                new_nums.append(val)
        output.append(new_nums)

        return output
        