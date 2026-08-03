import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {i : [] for i in range(len(points))}
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        minHeap = [[0, 0]]
        seen = set()
        result = 0
        while minHeap:
            dist, point = heapq.heappop(minHeap)

            if point in seen:
                continue

            result += dist
            seen.add(point)

            for neiCost, nei in adj[point]:
                if nei not in seen:
                    heapq.heappush(minHeap, [neiCost, nei])

        return result


            


       