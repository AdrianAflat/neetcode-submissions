class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list) # char patters : word group 

        for word in strs:
            letters = [0] * 26

            for char in word:
                letters[ord(char) - ord("a")] += 1
            
            seen[tuple(letters)].append(word)

        return list(seen.values())
