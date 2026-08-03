import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-x for x in nums]
        heapq.heapify(maxHeap)
        
        counter = k 
        result = 0
        while counter > 0:
            result = -(heapq.heappop(maxHeap))
            counter -= 1

        return result