class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split_s = s.split()
        reverse_split_s = reversed(split_s)

        for val in reverse_split_s:
            val = str(val)
            if len(val) > 0:
                if val[0].isalpha():
                    return len(val)

a = Solution()
b = a.lengthOfLastWord("Hello World")
print(b)