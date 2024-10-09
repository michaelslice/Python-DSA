# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res

            if root is None:
                return 0
            # Recursively find the height of the left and right subtree
            left = dfs(root.left)
            right = dfs(root.right)
            
            # The sum is the sum of the left and right heights
            res = max(res, left + right)

            # Return 1 + max, because the height is 1(the node itself)
            return 1 + max(left, right)
        
        dfs(root)
        return res

