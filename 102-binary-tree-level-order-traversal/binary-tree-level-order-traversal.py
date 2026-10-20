# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        
        ans = []

        queue = deque()
        queue.append(root)

        while queue:
            lvl = []
            lvl_len = len(queue)

            for i in range(lvl_len):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                lvl.append(node.val)
            
            ans.append(lvl)
        
        return ans