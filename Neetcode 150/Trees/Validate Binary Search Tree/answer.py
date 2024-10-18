# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            # Check if root node is null
            if not node:
                return True

            # Base case if left node is less than root node val
            # and the right node is less than node.val
            if not (left < node.val < right):
                return False

            # First part checks the right subtree, 
            # the other part checks the right subtree             
            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )
        # Initiate recursion, and initial bounds are set 
        # to infinity
        return valid(root, float("-inf"), float("inf"))