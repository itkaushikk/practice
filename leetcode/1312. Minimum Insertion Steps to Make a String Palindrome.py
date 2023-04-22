class Solution:
    def minInsertions(self, s: str) -> int:

        if s[:] == s[::-1]:
            return 0
        
        new_word = s
        no_of_check = int(len(s)/2)
        for index in range(no_of_check):
            end_index = -1-index

            if s[index] == new_word[end_index]:
                continue
            else:
                if s[index] == new_word[end_index-1]:
                    new_word = new_word[:index] + new_word[end_index] + new_word[index+1:]
                else:
                    new_word += s[index]
        
        no_of_check_after_initial = len(new_word[no_of_check:(len(new_word)-no_of_check)])

        word = new_word[no_of_check:(len(new_word)-no_of_check)]
        mid_word = word
        for index in range(int(no_of_check_after_initial)-1):
            if word[index] == mid_word[-1-index]:
                continue
            else:
                if word[index] == mid_word[-1-index-1]:
                    mid_word = mid_word[:index] + mid_word[-1-index] + mid_word[index:]
                else:
                    mid_word += word[index]
        
        new_word = new_word[:no_of_check] + mid_word + new_word[(len(new_word)-no_of_check):]
        
        return len(new_word)-len(s)


a = Solution()
b = a.minInsertions("zjveiiwvc")
print(b)