'''
Breadth-First-Search: Used to traverse a tree level by level,
implemented using a queue

Note: Explores level by level, good for finding shortest path
Note: Uses a queue

Steps to Perform BFS

1. Start at the root node and add it to the queue

2. While the queue is not empty
   Remove the front node from the queue
   Process the node
   Add all of its children to the queue(left child, right child)

3. Repeat until all nodes have been visited
'''
from collections import deque

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

def bfs_tree(root):
    if not root:
        return
    
    queue = deque([root]) # Initialize queue with root node

    while queue:
        node = queue.popleft() # Dequeue the front node
        print(node.value, end='')

        # Enqueue left child if it exists
        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

# Create a simple binary tree:
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

# Perform BFS
bfs_tree(root)