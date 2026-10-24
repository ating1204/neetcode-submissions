# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        DFS base case: if both trees are empty return true
        '''
        #both trees empty
        if not p and not q:
            return True
        if (p and not q) or (q and not p):
            return False
        if p.val != q.val:
            return False
        
        #up to root is the same
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

