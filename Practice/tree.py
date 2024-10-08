class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)    

def test():
    tree = BinaryTree(10)
    tree
    print("test")

if __name__ == "__main__":
    test()
    