# 0/1 Knapsack

## Concept

The 0/1 Knapsack problem asks us to maximize the total value of selected items without exceeding a given capacity.

Each item can either be selected once or not selected.

An item cannot be divided.

## When to Use

0/1 Knapsack is commonly useful when:

- Each item can be selected at most once.
- We need to maximize value under a capacity constraint.
- We need to choose between taking and skipping an item.
- The problem involves a limited resource.

## Example

Items:

Value = [60, 100, 120]

Weight = [10, 20, 30]

Capacity = 50

We choose the combination of items that gives the maximum value without exceeding capacity.

## DP State

dp[i][w] represents the maximum value using the first i items with capacity w.

For each item, we have two choices:

Do not take the item.

Take the item if it fits.

## Recurrence

If the item does not fit:

dp[i][w] = dp[i - 1][w]

Otherwise:

dp[i][w] = max(
    dp[i - 1][w],
    value[i - 1] + dp[i - 1][w - weight[i - 1]]
)

## Time Complexity

O(n * capacity).

## Space Complexity

O(n * capacity) for the standard DP table.

The space can be optimized to O(capacity).

## Common Mistake

Do not use the Fractional Knapsack greedy strategy for 0/1 Knapsack.

Items cannot be divided, so a greedy ratio-based approach does not always produce the optimal solution.

## Related Problems

Fractional Knapsack, Subset Sum, Partition Equal Subset Sum, Target Sum, and Coin Change.