'''
Dynamic Programming: Is a technique used to solve complex problems by breaking them down into simpler
    subproblems and solving each subrproblem only once, storing its result(usually in an array or table)
    to avoid redundant computations. Useful technique for problems that have overlapping subproblems 
    and optimal substructure

Dynamic Programming, can be summed up by recurance relations

Formula for Dynamic Programming Problems: Total = O(n * amount) * O(1) = O(n * amount)

Types of Dynamic Programming

1. Top-Down Approach (Memoization):
    In this approach, start by solving the main problem and break it into smaller
    subproblems as you go. As each subproblem is solved its result is stored in a
    table (usually array or hashmap). If the subrproblem is encountered again, you
    simply look up its result rather than solving again.
    
    Basically just recursion with caching(Which is just storing the results of expensive, function calls, and reusing result when same input occurs)

2. Bottom-Up Approach (Tabulation):
    In this approach you solve all the subproblems first, starting from the smallest one
    and use their soltion to build up to the main problem
    
    You use an iterative approach to fill a table with the solutions to all subproblems
    and then use that table to get the solution to the overall problem
'''