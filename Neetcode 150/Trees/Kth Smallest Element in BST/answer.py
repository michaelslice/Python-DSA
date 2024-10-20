# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Store out count of nodes, and the result node at k
        count = 0
        result = None
        # Perform DFS
        def dfs(root):
            # nonlocal allows us to manipulate these variables
            # declared in the outer function
            nonlocal count, result
            
            # Checking if we are at a leaf node
            # or if tree is empty
            # The other part checks if we found our result 
            if root is None or result is not None:
                return
            
            dfs(root.left)
            count += 1
            # Once the k-th smallest element is found we return
            if count == k:
                result = root.val
                return
            
            dfs(root.right)
        dfs(root)
        return result