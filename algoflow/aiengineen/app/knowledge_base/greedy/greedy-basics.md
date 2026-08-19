# Greedy Algorithms

## Concept

A greedy algorithm builds a solution step by step by choosing the best available option at each step.

The choice is made based on the current situation without reconsidering previous choices.

A greedy strategy works when local optimal choices can lead to a globally optimal solution.

## When to Use

Greedy algorithms are commonly useful when:

- The problem has an optimal substructure.
- A locally optimal choice can lead to a globally optimal solution.
- We need to minimize or maximize a quantity.
- The problem involves scheduling, intervals, or selection.
- Sorting can help determine the best order of choices.

## Example

Suppose we need to select the maximum number of non-overlapping activities.

Choose the activity that finishes earliest.

Then choose the next activity that starts after the selected activity finishes.

Continue until no more activities can be selected.

## General Approach

1. Identify the greedy choice.
2. Sort or organize the input if necessary.
3. Make the best available local choice.
4. Update the state.
5. Repeat until the solution is complete.
6. Verify that the greedy choice is globally valid.

## Time Complexity

Many greedy algorithms take O(n log n) time because they require sorting.

Some greedy algorithms can run in O(n).

## Space Complexity

Depends on the problem.

Many greedy solutions use O(1) extra space after sorting.

## Common Mistake

Do not assume that choosing the largest or smallest value is always correct.

A greedy strategy must have a valid proof or reasoning showing that the local choice can lead to an optimal solution.

## Related Problems

Activity Selection, Fractional Knapsack, Jump Game, Gas Station, Lemonade Change, Assign Cookies, Minimum Number of Arrows, and Merge Intervals.