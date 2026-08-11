class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''

        longestWord = max(len(word1), len(word2))
        for i in range(len(word1) + len(word2)):
            if word1 == '':
                res += (word2[0:])
                break
            if word2 == '':
                res += (word1[0:])
                break
            
            if i % 2 == 0:
                res += (word1[0])
                word1 = word1[1:]
            else:
                res += (word2[0])
                word2 = word2[1:]

        return res

            