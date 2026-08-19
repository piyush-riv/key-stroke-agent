# Tabulation

## Concept

Tabulation is a bottom-up Dynamic Programming technique that solves smaller subproblems first and uses their results to build larger solutions.

Instead of recursion, tabulation usually uses an iterative loop and a DP table.

## When to Use

Tabulation is commonly useful when:

- We can define a clear order for solving states.
- We want to avoid recursion.
- We want predictable memory usage.
- We want to optimize recursion-based DP.
- The problem has a natural sequence of smaller to larger states.

## Example

For Fibonacci:

F(0) = 0

F(1) = 1

Build the table from left to right:

dp[0] = 0

dp[1] = 1

dp[2] = dp[1] + dp[0]

dp[3] = dp[2] + dp[1]

Continue until dp[n].

## Algorithm

1. Define the DP table.
2. Initialize the base cases.
3. Determine the order in which states should be calculated.
4. Fill the table iteratively.
5. Return the required final state.

## Time Complexity

Depends on the number of states and transitions.

For Fibonacci:

O(n)

For a two-dimensional DP problem such as LCS:

O(m * n)

## Space Complexity

Depends on the DP table.

Fibonacci using a full table:

O(n)

Some problems can optimize the table to O(1) or O(n).

## Common Mistake

Do not fill the table without defining what each state represents.

Every dp[index] or dp[i][j] should have a clear meaning.

## Related Problems

Fibonacci, Climbing Stairs, Coin Change, 0/1 Knapsack, Longest Common Subsequence, Longest Increasing Subsequence, and Edit Distance.