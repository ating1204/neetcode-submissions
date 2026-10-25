# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        m = root.val
        def checkSide(root: TreeNode, m):
            if not root:
                return
            if root.val >= m:
                self.res += 1 
                m = root.val
            checkSide(root.left, m)
            checkSide(root.right, m)
        checkSide(root, m)
        return self.res
        



        