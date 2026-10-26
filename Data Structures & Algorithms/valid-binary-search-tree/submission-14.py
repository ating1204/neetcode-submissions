# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ''' 
        - start at root of the tree, with bounded -inf and inf
        - if the node doesnt fall within the range, then return false
        - otherwise, dfs with left and right, shrinking the bound to the node val

        - return True if node doesn't exist else check if valid if not valid ret false
        '''

        def dfs(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False

            return dfs(node.right, node.val, right) and dfs(node.left, left, node.val)

        return dfs(root, float("-inf"), float("inf"))