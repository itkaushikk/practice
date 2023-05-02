class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1

        for val in nums:
            if val > 0:
                product = product * 1
            elif val < 0:
                product = product * -1
            else:
                product = product * 0

        return product
