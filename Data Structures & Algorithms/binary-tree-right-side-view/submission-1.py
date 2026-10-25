# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.row = 0
        def dfs(r, k):
            if not r:
                return
            if k > self.row:
                res.append(r.val) 
                self.row += 1
                dfs(r.right, k+1)
                dfs(r.left, k+1)
            else:
                dfs(r.right, k+1)
                dfs(r.left, k+1)
        dfs(root, 1)
        return res
            
                

        