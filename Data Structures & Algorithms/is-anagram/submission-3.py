class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = [0] * 26
        word2 = [0] * 26

        for l in s:
            word1[ord(l) - ord('a')] += 1

        for l in t:
            word2[ord(l) - ord('a')] += 1

        if word1 == word2:
            return True
        else:
            return False
