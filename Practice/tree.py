'''


'''
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def maxDepth(root, depth=0):
    if root is None:
        print(f"Reached a leaf node, returning depth: {depth}")
        return depth
    
    print(f"At node {root.value} with current depth {depth}")
    
    left_depth = maxDepth(root.left, depth + 1)
    right_depth = maxDepth(root.right, depth + 1)
    
    max_depth = max(left_depth, right_depth)
    
    print(f"Returning from node {root.value} with max depth: {max_depth}")
    return max_depth

# Create a simple binary tree for testing
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Test the function
maxDepth(root)
