class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_val = max(candies)

        output = []

        for val in candies:
            if val+extraCandies >= max_val:
                output.append(True)
            else:
                output.append(False)
        
        return output