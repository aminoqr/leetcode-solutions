# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        ans = 0
        count = k
        def dfs(node):
            nonlocal count, ans
            if not node:
                return
            
            dfs(node.left)

            if count == 1:
                ans = node.val
            
            count -= 1

            if count > 0:
                dfs(node.right)
        
        dfs(root)
        return ans