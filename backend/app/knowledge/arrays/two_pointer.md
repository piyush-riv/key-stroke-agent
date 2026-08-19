# Two Pointer Technique

## Concept

The two pointer technique uses two indices that move through a data structure, usually an array or string.

The pointers may move toward each other, in the same direction, or at different speeds.

## When to Use

Two pointers are commonly useful when:

- The array is sorted.
- We need to find a pair of values.
- We need to compare elements from opposite ends.
- We need to reduce a nested loop into a linear scan.

## Example

Given a sorted array, we can use a left pointer at the beginning and a right pointer at the end.

If the sum of the two values is too small, move the left pointer forward.

If the sum is too large, move the right pointer backward.

## Time Complexity

Most two pointer solutions run in O(n) time.

## Space Complexity

Most basic two pointer solutions use O(1) extra space.

## Common Mistake

Do not automatically use two pointers on an unsorted array. Some two pointer techniques depend on the array being sorted.

## Related Problems

Two Sum on a sorted array, Pair Sum, Container With Most Water, and 3Sum.