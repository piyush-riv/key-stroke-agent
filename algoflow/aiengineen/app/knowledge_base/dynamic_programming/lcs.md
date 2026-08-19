# Longest Common Subsequence

## Concept

The Longest Common Subsequence, or LCS, problem asks for the longest sequence that appears in the same relative order in two strings.

The characters do not need to be contiguous.

## When to Use

LCS is commonly useful when:

- We compare two strings or sequences.
- Elements must remain in relative order.
- We need the longest common sequence.
- The problem involves matching or comparing sequences.

## Example

String 1:

"abcde"

String 2:

"ace"

The longest common subsequence is:

"ace"

Length:

3

## DP State

dp[i][j] represents the LCS length between the first i characters of the first string and the first j characters of the second string.

If the characters match:

dp[i][j] = dp[i - 1][j - 1] + 1

Otherwise:

dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

## Time Complexity

O(m * n)

where m and n are the lengths of the two strings.

## Space Complexity

O(m * n) for the standard DP table.

The space can sometimes be optimized to O(n).

## Common Mistake

Do not confuse subsequence with substring.

A subsequence does not need to be contiguous.

## Related Problems

Longest Common Substring, Edit Distance, Shortest Common Supersequence, Delete Operation for Two Strings, and Longest Palindromic Subsequence.