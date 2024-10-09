# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Note: We return a list of [balanced, height]
# 
# left[0]: Wether the left subtree is balanced
# left[1]: The height of the left subtree 
# right[0]: Wether the right subtree is balanced
# right[1]: The height of the left subtree
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Perform depth first search on the list
        def dfs(root):
            # Base case if the current node is empty
            if root is None:
                return [True, 0]
            # Recursively check the left and right subtree
            left, right = dfs(root.left), dfs(root.right)

            # A tree is balanced if both subtrees and their balanced heights differ by no more than 1
            # boolean variable
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            
            # Returns a tuple
            # - balanced: Wether the current subtree is balanced
            # - height: The height of the current subtree, which is 1 + (current node) + max height of the two subtrees
            return [balanced, 1 + max(left[1], right[1])]

        # Call dfs starting from root node
        return dfs(root)[0] 