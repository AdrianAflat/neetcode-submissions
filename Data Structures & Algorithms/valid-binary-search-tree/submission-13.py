# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        res = [True]
        def dfs(node, prevVal, left, right, minVal, maxVal): 
            if not node:
                return 

            if left and not (node.val < prevVal):
                res[0] = False 

            if right and not (node.val > prevVal):
                res[0] = False

            if not (minVal < node.val < maxVal):
                res[0] = False

            dfs(node.left, node.val, True, False, minVal, node.val)
            dfs(node.right, node.val, False, True, node.val, maxVal)


        dfs(root.left, root.val, True, False, float('-inf'), root.val)
        dfs(root.right, root.val, False, True, root.val, float('inf'))
        return res[0]


        #         0 
        #  -1000     1000
        #           0



