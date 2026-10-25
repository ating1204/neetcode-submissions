# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #dfs to smallest bst
        #if valid, 
        if not root:
            return True
        if self.isValidBST(root.left) and self.isValidBST(root.right):
            small, large = -float('inf'), float('inf')
            # print(root.val)
            if root.left:
                node = root.left
                while node.right:
                    node = node.right
                small = node.val
            if root.right:
                node = root.right
                while node.left:
                    node = node.left
                large = node.val
            # print(small, large) (27, inf)
            if small >= root.val or large <= root.val:
                return False
            else:
                return True
        return False

            
