# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs(root, subRoot):
            if not subRoot:
                return True
            if not root:
                return False

            if sameTree(root, subRoot):
                return True
            else:
                return dfs(root.right, subRoot) or dfs(root.left, subRoot)
            

        def sameTree(root, subRoot) -> bool:
            if (not root and subRoot) or (root and not subRoot):
                return False

            if not root and not subRoot:
                return True

            if root.val != subRoot.val:
                return False

            return sameTree(root.left, subRoot.left) and sameTree(root.right, subRoot.right)

        return dfs(root, subRoot)