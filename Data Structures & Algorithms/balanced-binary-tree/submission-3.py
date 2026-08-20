# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = [True]

        def height(node):
            if not node:
                return 0

            leftH = height(node.left)
            rightH = height(node.right)

            if abs(leftH - rightH) > 1:
                res[0] = False

            return 1 + max(leftH, rightH)

        height(root)
        return res[0]

