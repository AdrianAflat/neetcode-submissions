import heapq

class MedianFinder:

    def __init__(self):
        self.maxHeap = [] # stores the lower half of values
        self.minHeap = [] # stores the upper half of values 

    def addNum(self, num: int) -> None:
        if not self.minHeap:
            heapq.heappush(self.minHeap, num)
            return
            
        minValue = self.minHeap[0]
        if num > minValue:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)

        minHeapLen = len(self.minHeap)
        maxHeapLen = len(self.maxHeap)

        if minHeapLen - maxHeapLen > 1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)
        elif maxHeapLen - minHeapLen > 1:
            val = -(heapq.heappop(self.maxHeap))
            heapq.heappush(self.minHeap, val)

    def findMedian(self) -> float:
        minHeapLen = len(self.minHeap)
        maxHeapLen = len(self.maxHeap)
        result = 0.0

        if minHeapLen > maxHeapLen:
            result = self.minHeap[0]
        elif maxHeapLen > minHeapLen:
            result = -(self.maxHeap[0])
        else:
            num1 = self.minHeap[0]
            num2 = -(self.maxHeap[0])
            result = (num1 + num2) / 2
        
        return result
