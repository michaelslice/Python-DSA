'''
Recursion: Refers to a functio calling itself to solve a problem in smaller 
simpler steps. The recursive solution generally breaks down complex problems
into smaller sub-problems until it reaches a base case.

Best Situations to Use Recursion:
1. Problems that can be broken down into similiar sub problems(fibonacci, factorial, tree traversal)
2. Recursive Algorithms: Good for Depth-First-Search, easier to write than iterative approach

Key Components:
1. Base Case: Condition that ends the recursion, without a base case we will get stack overflow
2. Recursive Case: The part where the function calls itself, reducing the problem into smaller instances

General Steps to Solving any Problem Recursively:
1. Find the simplest case (base case)
2. Play around with examples and visualize
3. Relate the harder cases to the simpler case
4. Generalize the pattern
5. Combine recursive pattern with base case using code 

Example Recursive Problem the fibonacci sequence...
'''
def fib(n: int) -> int:
    if n > 1:
        return fib(n - 1) + fib(n - 2)
    else:
        return n
print(fib(5))
'''
When you call fib(5), the function splits the problem into fib(4) + fib(3) and continues this process...

For example:

fib(5) -> fib(4) + fib(3)
fib(4) -> fib(3) + fib(2)
fib(3) -> fib(2) + fib(1)
fib(2) -> fib(1) + fib(0)

Base Case: fib(1) returns 1, and fib(0) returns 0
'''