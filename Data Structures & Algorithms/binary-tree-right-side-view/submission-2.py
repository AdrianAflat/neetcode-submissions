# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []

        q = deque()
        q.append(root)
        while q:
            level = []
            for i in range(len(q)):
                temp = q.popleft()

                if i == 0:
                    res.append(temp.val)

                if temp.right:
                    q.append(temp.right)
                if temp.left:
                    q.append(temp.left)
        
        return res