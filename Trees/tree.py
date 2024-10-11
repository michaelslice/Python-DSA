'''
Definition for a binary tree node.

Tree Structure: A binary tree consists of nodes, where 
each node has at most two children: a left child, and a right child
Root: Is the top most node of the tree
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right