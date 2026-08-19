# Dynamic Programming Basics

## Concept

Dynamic Programming, or DP, is a technique used to solve problems by breaking them into smaller overlapping subproblems and storing their results.

DP avoids solving the same subproblem repeatedly.

A DP solution usually requires:

- A state that represents a subproblem.
- A recurrence or transition between states.
- Base cases.
- A way to store previously calculated results.

## When to Use

Dynamic programming is commonly useful when:

- The problem has overlapping subproblems.
- The problem has optimal substructure.
- A recursive solution repeats the same calculations.
- We need to find a minimum, maximum, count, or number of ways.
- The problem involves decisions over a sequence.

## Example

Fibonacci numbers:

F(n) = F(n - 1) + F(n - 2)

Without storing results, the same Fibonacci values are calculated repeatedly.

With DP, calculate each value once.

For:

F(0) = 0

F(1) = 1

F(2) = 1

F(3) = 2

F(4) = 3

## Two Main Approaches

Top-down DP uses recursion with memoization.

Bottom-up DP uses an iterative table and starts from the base cases.

## Time Complexity

Depends on the number of states and transitions.

A common DP solution runs in O(n) or O(n²).

## Space Complexity

Depends on the number of stored states.

A typical DP table may require O(n) or O(n²) space.

Some problems can optimize the space to O(1) or O(n).

## Common Mistake

Do not immediately use DP just because recursion is involved.

First determine whether subproblems overlap and whether previous results can be reused.

Also define the DP state clearly before writing the recurrence.

## Related Problems

Fibonacci, Climbing Stairs, House Robber, Coin Change, 0/1 Knapsack, Longest Common Subsequence, Longest Increasing Subsequence, and Edit Distance.