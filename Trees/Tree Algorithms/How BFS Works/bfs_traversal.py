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
'''
from collections import deque

def bfs_tree(root):
    if not root:
        return
    
    queue = deque([root])  # Initialize queue with root node

    while queue:
        node = queue.popleft()  # Dequeue the front node
        print(node.value, end=' ')  # Process the node (print its value)

        # Enqueue left child if it exists
        if node.left:
            queue.append(node.left)

        # Enqueue right child if it exists
        if node.right:
            queue.append(node.right)
