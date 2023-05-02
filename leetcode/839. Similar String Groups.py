class Solution:
    def numSimilarGroups(self, strs) -> int:
        output = 0

        for i in range(len(strs)):
            for r in range(i+1, len(strs)):
                word1 = strs[i]
                word2 = strs[r]

                if word1 == word2:
                    output += 1
                else:
                    for ii in range(len(word1)):
                        for ir in range(ii+1, len(word2)):
                            new_word = word2[ir] + word2[ii+1:ir] + word2[ii] + word2[ir+1:]
                            if word1 == new_word:
                                output += 1
                                break
        
        return output

a = Solution()
b = a.numSimilarGroups(["omv","ovm"])
print(b)