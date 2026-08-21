# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val, None, None)

        cur = root
        while True:
            if not cur:
                return None

            if cur.val < val and not cur.right:
                cur.right = TreeNode(val, None, None)
                break
            if cur.val > val and not cur.left:
                cur.left = TreeNode(val, None, None)
                break

            if cur.val < val:
                cur = cur.right
            elif cur.val > val:
                cur = cur.left

        return root