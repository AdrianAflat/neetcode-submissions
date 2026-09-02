class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        letterIndex = {} # letter in word : index in the alien dictionary
        for i in range(len(order)):
            letterIndex[order[i]] = i

        if len(words) == 1:
            return True

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for j in range(len(w1)):
                if j == len(w2):
                    return False 

                if w1[j] != w2[j]:
                    if letterIndex[w1[j]] > letterIndex[w2[j]]:
                        return False
                    break

        return True
              