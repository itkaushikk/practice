class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:
            max_val = max(stones)
            stones.remove(max_val)

            second_max_val = max(stones)
            stones.remove(second_max_val)

            diff_val = max_val - second_max_val

            if diff_val != 0 or stones == []:
                stones.append(diff_val)
        
        return stones[0]
