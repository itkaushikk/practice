class Solution:
    def bulbSwitch(self, n: int) -> int:
#         all_bulbs = []
# 
#         #first round
#         for i in range(n):
#             all_bulbs.append("on")
#         
#         for i in range(1, n):
#             for r in range(i, n, i+1):
#                 if all_bulbs[r] == "on":
#                     all_bulbs[r] = "off" 
#                 else:
#                     all_bulbs[r] = "on"
#         
#         return all_bulbs.count("on")
          import math
          return math.isqrt(n)

a = Solution()
b = a.bulbSwitch(3)
print(b)