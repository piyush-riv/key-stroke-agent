# Memoization

## Concept

Memoization is a top-down Dynamic Programming technique that uses recursion and stores the result of previously solved subproblems.

When the same subproblem appears again, its stored result is reused instead of calculating it again.

## When to Use

Memoization is commonly useful when:

- A recursive solution contains overlapping subproblems.
- The same state is calculated multiple times.
- We want to convert a recursive solution into a DP solution.
- The problem naturally follows a recursive structure.

## Example

For Fibonacci:

F(n) = F(n - 1) + F(n - 2)

Without memoization, the same Fibonacci values are calculated repeatedly.

With memoization, once F(3) is calculated, its result is stored and reused whenever F(3) is needed again.

## Algorithm

1. Define a recursive function representing the state.
2. Check whether the current state has already been calculated.
3. If it has, return the stored result.
4. Otherwise, calculate the result recursively.
5. Store the result.
6. Return the result.

## Time Complexity

Usually O(number of states × transitions per state).

For Fibonacci, the time complexity becomes O(n).

## Space Complexity

O(n) for the memoization table plus O(n) recursion stack in many one-dimensional problems.

## Common Mistake

Do not forget to check the memoization table before performing the recursive calculation.

Also initialize uncomputed states carefully so they can be distinguished from valid results.

## Related Problems

Fibonacci, Climbing Stairs, House Robber, Coin Change, 0/1 Knapsack, Longest Common Subsequence, and Longest Increasing Subsequence.