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
                return 0
            l = collapse(root.left)
            r = collapse(root.right)
            m = max(root.val + r, root.val + l)
            self.res = max(root.val, l + r + root.val, m, self.res)

            return max(root.val, m, 0)

        collapse(root)
        return self.res