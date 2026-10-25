# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = deque([(root, root.val)])
        count = 0
        while queue:
            n = len(queue)
            for _ in range(n):
                r, m = queue.popleft()
                if r.val >= m:
                    m = r.val
                    count += 1
                if r.left:
                    queue.append([r.left, m])
                if r.right:
                    queue.append([r.right, m])
        return count
