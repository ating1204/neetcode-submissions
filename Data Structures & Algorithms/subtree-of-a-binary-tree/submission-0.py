# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #base case: root == None
        #base case 2: same root value, isSameTree

        if not root:
            return False
        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True
        
        #check if subtrees are valid
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, r1: Optional[TreeNode], r2: Optional[TreeNode]):
        #same question, DFS recursion

        if not r1 and not r2:
            return True
        #either r1 or r2 is none (one or other)
        if not r1 or not r2:
            return False
        if r1.val != r2.val:
            return False
        
        return self.isSameTree(r1.left, r2.left) and self.isSameTree(r1.right, r2.right)


        