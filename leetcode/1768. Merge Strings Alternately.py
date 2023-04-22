class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_len = 0
        if len(word1) > len(word2):
            max_len = len(word1)
        else:
            max_len = len(word2)
        
        new_seq = ""
        for i in range(max_len):
            if len(word1) > i:
                new_seq += word1[i]
            
            if len(word2) > i:
                new_seq += word2[i]
        
        return new_seq
