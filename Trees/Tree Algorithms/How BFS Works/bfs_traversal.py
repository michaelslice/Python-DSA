'''
Queue: Follows first in first out

Dequeue: Adding a element to the back of the queue  
Enqueue Remove the first element in the queue

What is BFS?
BFS is a way to visit all nodes in a tree or graph, starting from the top(root) 
and exploring the tree level by level, meaning it visits all nodes at the same depth before going deeper

Imagine this tree...
       1
     /   \
    2     3
   / \   / \
  4   5 6   7

Goal: Visit every node, starting from the root(1), and print their values, level by level

The queue stores the nodes to be processed. As each node is processed, its children are added to the queue for future processing.
'''
from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# BFS function
def bfs(root):
    if root is None:
        return

    queue = deque([root])  # Initialize the queue with the root node
    print(f"Initial queue: {[node.value for node in queue]}")
    
    while queue:
        current = queue.popleft()  # Dequeue the front node
        print(f"\nProcessing node: {current.value}")
        print(f"Queue after dequeue: {[node.value for node in queue]}")

        # Process the current node (printing its value in this case)
        print(f"Visited node: {current.value}")

        # Enqueue the left child
        if current.left:
            queue.append(current.left)
            print(f"Enqueued left child: {current.left.value}")
        
        # Enqueue the right child
        if current.right:
            queue.append(current.right)
            print(f"Enqueued right child: {current.right.value}")
        
        # Print the current state of the queue
        print(f"Queue after enqueuing children: {[node.value for node in queue]}")

# Example tree construction:
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

# Run BFS
bfs(root)
