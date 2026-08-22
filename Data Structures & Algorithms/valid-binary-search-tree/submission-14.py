# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = [True]
        def valid(node, left, right):
            if not node:
                return 

            if not (node.val < right and node.val > left):  
                res[0] = False

            valid(node.left, left, node.val)
            valid(node.right, node.val, right)

        valid(root, float('-inf'), float('inf'))
        return res[0]