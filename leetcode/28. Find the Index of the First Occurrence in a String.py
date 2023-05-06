class Solution:
    def strStr(self, haystack: str, needle: str):
        length_of_needle = len(needle)
        length_of_haystack = len(haystack)

        for i in range(length_of_haystack-length_of_needle+1):
            word = haystack[i:length_of_needle+i]

            if word == needle:
                return i
        
        return -1
        
        
a = Solution()
b = a.strStr(haystack = "hello", needle = "ll")
print(b)