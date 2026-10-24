# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #if p or q is root, return root
        if root.val == p.val or root.val == q.val:
            return root

        #if p and q on diff sides, return root
        #return if not TT or FF
        left1 = self.detSide(root.left, p) 
        left2 = self.detSide(root.left, q)
        if (left1 ^ left2):
            return root
        else:
            #p on left, q on left 
            if left1:
                return self.lowestCommonAncestor(root.left, p, q)
            #p, q on right
            else:
                return self.lowestCommonAncestor(root.right, p, q)

    def detSide(self, root: TreeNode, t: TreeNode):
        if not root:
            return False
        if root.val == t.val:
            return True
        return self.detSide(root.left, t) or self.detSide(root.right, t)
        