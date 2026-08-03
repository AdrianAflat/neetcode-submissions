import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        # [10 10 7 2]
        # []

        while len(maxHeap) > 1:
            x = -(heapq.heappop(maxHeap)) # 7
            y = -(heapq.heappop(maxHeap)) # 2
            print(maxHeap)
             
            if x < y:
                y = y - x  
                heapq.heappush(maxHeap, -y)
            elif x > y:
                x = x - y
                heapq.heappush(maxHeap, -x)
            else:
                continue
            
        if len(maxHeap) < 1:
            return 0
        else:
            return -(heapq.heappop(maxHeap))

        
        