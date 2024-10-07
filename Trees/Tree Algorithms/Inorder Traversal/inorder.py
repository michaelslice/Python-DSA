class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
Inorder traversal is going through all nodes in left subtree and going
through right subtree

'''
def inorder(node):
    if node:
        inorder(node.left) # Traverse the left subtree
        print(node.val, end=" ") # Visit the current node  
        inorder(node.right) # Traverse the right subtree

def preorder(node):
    if node:
        print(node.val, end=" ") # Visit root
        preorder(node.left) # Visit left subtree
        preorder(node.right) # Visit right subtree

def postorder(node):
    if node:
        postorder(node.left) # Vist left subtree 
        postorder(node.right) # Vist right subtree 
        print(node.val, end=" ") # Visit root 
        