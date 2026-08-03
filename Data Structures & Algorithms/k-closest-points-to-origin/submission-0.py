import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # create map of distance : [x, y]
        # make heap of distances 
        # pop smallest distances and return the points associated with them

        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)

        result = []
        while len(result) < k:
            dist, x, y = heapq.heappop(minHeap)
            result.append([x, y])

        return result
