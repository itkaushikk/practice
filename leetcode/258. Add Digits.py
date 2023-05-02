class Solution:
    def addDigits(self, num: int) -> int:

        str_num = str(num)

        while len(str_num) > 1:
            sum_num = 0

            for val in str_num:
                sum_num += int(val)
            
            str_num = str(sum_num)
        
        return int(str_num)