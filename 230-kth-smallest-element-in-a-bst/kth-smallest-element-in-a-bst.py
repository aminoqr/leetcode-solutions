# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        listt = []
        def process(node):
            if node.left:
                process(node.left)
            listt.append(node.val)
            if node.right:
                process(node.right)
        
        process(root)
        return listt[k-1]