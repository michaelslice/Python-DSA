'''
When we traverse a tree we mostly use recursion by the Depth-First-Search algorithm

How DFS works with Recursion:
When you call dfs(root)...
1. If root is None you return (base case)
2. Otherwise you perform some operation on the current node
3. Then you call dfs(root.left), to explore the left subtree
4. After that you call dfs(root.right), to explore right subtree

Given the following tree...
       1
      / \
     2   3
    / \
   4   5

When we call dfs(1) the steps are as follows...
1. Call dfs(1):
    Print(1)
    Call dfs(1.left) -> dfs(2)

2. Call dfs(2):
    Print(2)
    Call dfs(2.left) -> dfs(4)

3. Call dfs(4):
    Print(4)
    Call dfs(4.left) -> dfs(none) (Base case returns)
    Call dfs(4.right) -> dfs(none) (Base case returns)
    Return to dfs(2)
    
4. Back to dfs(2)
    Call dfs(2.right) -> dfs(5)

5. Call dfs(5)
    Print(5)
    Call dfs(5.left) -> dfs(none) (Base case returns)
    Call dfs(5.right) -> dfs(none) (Base case returns)
    Return to dfs(2)

6. Return to dfs(1) (after processing left subtree)
    Call dfs(1.right) -> dfs(3)
    
7. Call dfs(3)
    Print(3)
    Call dfs(3.left) -> dfs(none) (Base case returns)
    Call dfs(3.right) -> dfs(none) (Base case returns)
    Returns to dfs(1)

'''

'''
How Backtracking Works in Recursion

1. Call Stack: When you make a function call, that call is placed
on the call stack. The call stack is a structure that keeps track
of active function calls. Each call has its own context

2. Recursive Calls: When you call a function recursively 
like dfs(root.left), a new frame is added to the call stack 
for that call. This frame contains the context for the the new
function call, including the current node being processed.

3. Base Case and Returning: When you reach a leaf node(a node
that has no children), the next calls dfs(node.left) and dfs(node.right)
will encounter node as None, which hits the base case of the recursion `if node is None: return`
at this point the function returns back to the previous call(the parent node)

Backtracking Summary:
1. When a function call reaches its base case, it returns to the previous call
2. Each time a function returns, it resumes execution from the point right after where it
made the call to the function that just returned it
3. The tree traversal continues until all nodes have been visisted, at which point all recursive 
calls have returned, and the entire DFS operation is complete 

Example of Backtracking
       1
      / \
     2   3
    / \
   4   5

1. Initial Call: dfs(1)
    Call Stack: dfs(1)
    
2. Move to Left Child: Inside dfs(1), you call dfs(2)
    Call Stack: dfs(1), dfs(2)
    
3. Move to Left Child Again: Inside dfs(2), you call dfs(4)
    Call Stack: dfs(1), dfs(2), dfs(4)
    
4. Hit Leaf Node: Inside dfs(4), you call dfs(4.left) (which is None)
    Call Stack: dfs(1), dfs(2), dfs(4), dfs(None)
    
5. Base Case Triggered: dfs(None) hits the base case and returns.
    Now the call stack looks like this...
    Call Stack: dfs(1), dfs(2), dfs(4) (backtracking to dfs(4))
    
6. Continue from Leaf Node: After the call to dfs(4.left) returns, you now call dfs(4.right) (which is also None).
    Call stack: dfs(1), dfs(2), dfs(4), dfs(None)

7. Base Case Triggered Again: The call to dfs(None) returns, bringing us back to dfs(4).
    Call stack: dfs(1), dfs(2) (backtracking to dfs(2))

8. Back to Parent Node: Now you're back in dfs(2), and since you finished processing dfs(4), 
    you proceed to call dfs(2.right) (which is 5).
    Call stack: dfs(1), dfs(2), dfs(5)
9. Process Node 5: This process continues until all nodes are processed, 
    and you ultimately return back to the initial call dfs(1) after processing both children.
'''
