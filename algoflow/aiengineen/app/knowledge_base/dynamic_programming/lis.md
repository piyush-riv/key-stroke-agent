# Longest Increasing Subsequence

## Concept

The Longest Increasing Subsequence, or LIS, is the longest subsequence of an array in which the elements are strictly increasing.

The elements do not need to be adjacent.

## When to Use

LIS is commonly useful when:

- We need the longest increasing sequence.
- Elements do not need to be contiguous.
- The problem involves selecting elements while maintaining increasing order.
- We need to compare different subsequences.

## Example

Given:

[10, 9, 2, 5, 3, 7, 101, 18]

One longest increasing subsequence is:

[2, 3, 7, 101]

Its length is:

4

Another valid LIS is:

[2, 5, 7, 101]

## DP State

dp[i] represents the length of the longest increasing subsequence ending at index i.

For every previous index j:

If:

nums[j] < nums[i]

then:

dp[i] = max(dp[i], dp[j] + 1)

## Time Complexity

The basic DP solution takes O(n²).

An optimized solution using binary search takes O(n log n).

## Space Complexity

O(n).

The DP solution requires an array to store the best subsequence length for each position.

## Common Mistake

Do not confuse a subsequence with a subarray.

A subsequence does not need to be contiguous.

Also remember that increasing usually means strictly increasing unless the problem explicitly allows equal values.

## Related Problems

Longest Non-decreasing Subsequence, Russian Doll Envelopes, Maximum Length of Pair Chain, Longest Common Subsequence, and Number of Longest Increasing Subsequences.