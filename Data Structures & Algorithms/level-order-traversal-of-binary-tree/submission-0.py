# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque()
        queue.append(root)

        while queue:
            level = []
            n = len(queue)

            for i in range(n):
                node = queue.popleft()
                level.append(node.val)

                if node.left: 
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result
        
        
            


            