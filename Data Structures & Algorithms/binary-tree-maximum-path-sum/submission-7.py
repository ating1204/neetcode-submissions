# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        def collapse(root: Optional[TreeNode]) -> int:
            if not root:
                return -1000000
            l = collapse(root.left)
            r = collapse(root.right)

            self.res = max(root.val, l + r + root.val, root.val + r, root.val + l, self.res)

            return max(root.val, root.val + l, root.val + r, 0)
        collapse(root)
        return self.res