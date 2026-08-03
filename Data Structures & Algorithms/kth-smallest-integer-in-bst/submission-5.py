# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = [0]
        count = [k]
        def dfs(root):
            if not root:
                return None

            dfs(root.left)
                
            if count[0] == 1:
                ans[0] = root.val
            
            count[0] = count[0] - 1

            if count[0] > 0: 
                dfs(root.right)

        dfs(root)
        return ans[0]