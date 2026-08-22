# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]

        def dfs(node, maxVal):
            if not node:
                return None

            if node.val >= maxVal:
                res[0] += 1

            dfs(node.left, max(node.val, maxVal))
            dfs(node.right, max(node.val, maxVal))

        dfs(root, float('-inf'))
        return res[0]
 
        #      3
        #   3     None
        # 4   2