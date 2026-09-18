class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = defaultdict(list) # pattern : indexes with that pattern
        for i, word in enumerate(strs):
            pattern = [0] * 26
            for l in word:
                pattern[ord(l) - ord('a')] += 1
            strMap[tuple(pattern)].append(i)

        res = []
        for key in strMap:
            subList = []
            for val in strMap[key]:
                subList.append(strs[val])
            res.append(subList.copy())
            subList.clear()

        return res