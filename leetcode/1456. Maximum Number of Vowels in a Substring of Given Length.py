class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowels_count = 0

        for i in range(len(s)-k+1):
            sub_string = s[i:k+i]

            vowels_count = 0
            a_vowels = sub_string.count("a")
            e_vowels = sub_string.count("e")
            i_vowels = sub_string.count("i")
            o_vowels = sub_string.count("o")
            u_vowels = sub_string.count("u")
            vowels_count = a_vowels + e_vowels + i_vowels + o_vowels + u_vowels
            
            if vowels_count > max_vowels_count:
                max_vowels_count = vowels_count
            
            if max_vowels_count == k:
                break
        
        return max_vowels_count