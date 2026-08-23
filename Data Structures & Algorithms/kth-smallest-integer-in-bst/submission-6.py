# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        minHeap = []
        def dfs(node):
            if not node:
                return None

            heapq.heappush(minHeap, node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        res = 0
        for n in range(k):
            temp = heapq.heappop(minHeap)
            res = temp

        return res