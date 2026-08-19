# Coin Change

## Concept

The Coin Change problem asks for the minimum number of coins needed to make a given amount using available coin denominations.

Each coin can usually be used unlimited times.

## When to Use

Coin Change is commonly useful when:

- We need a minimum number of elements.
- Choices can be reused.
- The problem involves making a target amount.
- A greedy solution does not always work.

## Example

Coins:

[1, 2, 5]

Amount:

11

The minimum number of coins is:

5 + 5 + 1

Answer:

3

## DP State

dp[x] represents the minimum number of coins needed to make amount x.

For every coin:

dp[x] = min(dp[x], dp[x - coin] + 1)

## Base Case

dp[0] = 0

An amount of zero requires zero coins.

## Time Complexity

O(amount * number of coins).

## Space Complexity

O(amount).

## Common Mistake

Do not assume that choosing the largest available coin always produces the optimal answer.

Greedy works for some coin systems but not for all possible denominations.

## Related Problems

Coin Change II, 0/1 Knapsack, Combination Sum, Minimum Cost Problems, and Unbounded Knapsack.