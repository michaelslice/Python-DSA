# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Store the final result of the nodes
        res = []

        # Queue to keep track of nodes at the current level
        queue = collections.deque()
        
        # If the root is not null, add it to the queue to start traversal
        if root:
            queue.append(root)

        # While there are nodes continue process
        while queue:

            # Temp list to hold nodes at current level
            val = []    

            # Iterate through all nodes at current level
            for i in range(len(queue)):

                # Remove the leftmost node from the queue 
                node = queue.popleft()
                # Add the nodes value to the current level's list
                val.append(node.val)

                # If the node has a left child, add it to the queue to process in the next level
                if node.left:
                    queue.append(node.left)
                # If the node has a right child, add it to the queue to process in the next level
                if node.right:
                    queue.append(node.right)
            # After processing all nodes in current level, add the levels values to result
            res.append(val)
        # 
        return res