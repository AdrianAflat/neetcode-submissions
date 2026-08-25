# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root or root.val == target:
            return None
        
        def dfs(node, prev):
            if not node:
                return 

            node.left = dfs(node.left, node)
            node.right = dfs(node.right, node)

            if node.val == target and not node.right and not node.left:
                return None
            
            return node


        dfs(root, None)
        return root