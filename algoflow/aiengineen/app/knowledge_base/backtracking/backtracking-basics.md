# Backtracking Basics

## Concept

Backtracking is a problem-solving technique that builds a solution step by step and abandons a partial solution when it cannot lead to a valid complete solution.

It explores possible choices using recursion.

The general pattern is:

Choose → Explore → Undo

## When to Use

Backtracking is commonly useful when:

- We need to generate all possible solutions.
- The problem involves combinations or permutations.
- We need to explore different choices.
- A partial solution can be rejected early.
- The problem has constraints that can prune invalid choices.

## Example

For generating subsets of:

[1, 2]

Start with:

[]

Choose 1:

[1]

Choose 2:

[1, 2]

Undo 2:

[1]

Undo 1.

Choose 2:

[2]

The subsets are:

[]

[1]

[2]

[1, 2]

## General Algorithm

1. Make a choice.
2. Add the choice to the current solution.
3. Recursively explore the next choices.
4. Undo the choice.
5. Try another choice.

## Time Complexity

Depends on the number of possible choices.

Many backtracking problems have exponential time complexity.

## Space Complexity

Usually O(depth) for the recursion stack, excluding the output.

## Common Mistake

Do not forget to undo the choice after returning from recursion.

Without backtracking, choices from one branch can incorrectly affect another branch.

## Related Problems

Subsets, Permutations, Combination Sum, N-Queens, Sudoku Solver, Word Search, and Generate Parentheses.