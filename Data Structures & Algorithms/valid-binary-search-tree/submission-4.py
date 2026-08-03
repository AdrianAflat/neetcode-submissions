# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = [True]

        def search(root, low, high):
            if not root:
                return None

            if not (low < root.val < high):
                result[0] = False

            search(root.left, low, root.val) 
            search(root.right, root.val, high)

        search(root, float('-inf'), float('inf'))
        return result[0]