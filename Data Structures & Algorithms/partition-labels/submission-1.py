class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        indexMap = {}
        for index, char in enumerate(s):
            indexMap[char] = index

        result = []
        size = 0
        end = 0
        
        for index, char in enumerate(s):
            size += 1
            end = max(end, indexMap[char])

            if index == end: 
                result.append(size)
                size = 0

        return result
