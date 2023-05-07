class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        no_of_elements = len(nums)
        nums_diff = []
        
        for i in range(no_of_elements):
            #prefix distinct elements
            repeated_elements = []
            prefix_count = 0
            for r in range(i+1):
                if nums[r] not in repeated_elements:
                    prefix_count += 1
                    repeated_elements.append(nums[r])
            
            #suffix distinct elements
            repeated_elements = []
            suffix_count = 0
            for r in range(i+1, no_of_elements):
                if nums[r] not in repeated_elements:
                    suffix_count += 1
                    repeated_elements.append(nums[r])
            
            diff_val = prefix_count - suffix_count
            nums_diff.append(diff_val)
        
        return nums_diff
        

a = Solution()
b = a.distinctDifferenceArray([3,2,3,4,2])
print(b)