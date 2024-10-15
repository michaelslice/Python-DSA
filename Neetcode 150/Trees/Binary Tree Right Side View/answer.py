# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # If root empty, then empty right side view
        if root is None:
            return []
        
        # Queue used for BSF
        queue = deque([root])
        # Answer list
        ans = []

        # While there are nodes in the tree
        while queue:
            # Temp list to store nodes at current level
            val = []
            # Iterate through all nodes at current level
            for i in range(len(queue)):
                node = queue.popleft()
                val.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # We only care about the nodes at the right, so index -1
            ans.append(val[-1])
            
        return ans