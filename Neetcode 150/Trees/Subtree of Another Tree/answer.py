# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If subRoot is empty, it is a subtree of any tree
        if not subRoot:
            return True 
        # If root is empty, but not subRoot, then subRoot cannot be a subtree of root
        if not root:
            return False
        
        # Check if root and subRoot are identical Trees 
        if self.sameTree(subRoot, root):
            return True
        # Recursively check if subRoot is a subTree of the left or right child of root
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # Helper function to check if both trees are identical
    def sameTree(self, root, subRoot):
        # If both trees are empty, they are identical
        if not root and not subRoot:
            return True
        # If both trees are non empty and their root values are the same, check if 
        # their left and right subtrees are identical
        if root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        
        # If one tree is empty or their values dont match the trees are not identical
        return False