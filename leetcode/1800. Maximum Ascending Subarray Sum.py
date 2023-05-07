class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        largest_sum_of_subarray = nums[0]

        for i in range(len(nums)):
            sub_array = [nums[i]]
            for r in range(i+1, len(nums)):
                if nums[r] <= nums[r-1]:
                    break
                sub_array.append(nums[r])

                if sum(sub_array) > largest_sum_of_subarray:
                    largest_sum_of_subarray = sum(sub_array)
        
        return largest_sum_of_subarray