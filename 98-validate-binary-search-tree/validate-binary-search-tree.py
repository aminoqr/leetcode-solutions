# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def isvalid(node, minn, maxx):
            if not node:
                return True

            if not minn < node.val < maxx:
                return False

            left = isvalid(node.left, minn, node.val)
            right = isvalid(node.right, node.val, maxx)

            return left and right


        return isvalid(root, float('-inf'), float('inf'))