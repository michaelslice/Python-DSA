# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If either tree is empty
        if not p and not q:
            return True
        # If either tree is empty
        if not p or not q:
            return False
        # If the values are not the samae 
        if p.val != q.val:
            return False  

        # If left tree and right tree are the same return true
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))