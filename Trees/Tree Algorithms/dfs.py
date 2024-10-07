'''
Depth-First-Search: Explores as far down a branch as possible
before backtracking, implementing using a stack

Note: Explores one branch entirely before backtracking 
Note: Uses a stack

Key DFS Traversal Types on Trees
1. Preorder Traversal (DFS): Visit the node then recursively 
   visit the left and right subtree
2. Inorder traversal (DFS): Recursively visit the left subtree, visit 
   the node, then recursively visit the right subtree 
3. Postorder Traversal (DFS): Recursively visit the left and right subtree 
   then visit the node
'''
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
'''
DFS Preorder Traversal Root->Left->Right

In preorder traversal the order is...

Visit the Node
Recursively visit the left subtree
Recursively visist the right subtree
'''
def dfs_preorder(root):
    if root is None:
        return
    print(root.value, end=' ')  # Process the current node
    dfs_preorder(root.left)     # Traverse the left subtree
    dfs_preorder(root.right)    # Traverse the right subtree

# Example binary tree:
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Perform DFS Preorder Traversal
dfs_preorder(root)

'''
DFS Inorder Traversal Left -> Root-> Right

In inorder traversal, the order is...

Recursively visit the left subtree.
Visit the node.
Recursively visit the right subtree.
'''
def dfs_inorder(root):
    if root is None:
        return
    dfs_inorder(root.left)      # Traverse the left subtree
    print(root.value, end=' ')  # Process the current node
    dfs_inorder(root.right)     # Traverse the right subtree

# Perform DFS Inorder Traversal
dfs_inorder(root)
'''
DFS Postorder Traversal Left-> Right-> Root
In postorder traversal, the order is...

Recursively visit the left subtree.
Recursively visit the right subtree.
Visit the node.
'''
def dfs_postorder(root):
    if root is None:
        return
    dfs_postorder(root.left)    # Traverse the left subtree
    dfs_postorder(root.right)   # Traverse the right subtree
    print(root.value, end=' ')  # Process the current node

# Perform DFS Postorder Traversal
dfs_postorder(root)

'''
Iterative DFS Using a Stack
'''
def dfs_preorder_iterative(root):
    # Base case, if the node has no children then it is None
    if root is None:
        return
    
    stack = [root] # Initialize stack with root node

    while stack:
        node = stack.pop() # Get the current node
        print(node.value, end=' ') # Process the node

        # Push right child first (so that the left is processed first, since stack is LIFO)
        if node.right:
            stack.append(node.right)

        # Push left child
        if node.left:
            stack.append(node.left)
