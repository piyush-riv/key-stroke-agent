# Binary Search

## Concept

Binary search is an efficient searching algorithm that repeatedly divides a sorted search space into two halves.

If the middle element is not the target, one half of the search space can be eliminated.

## When to Use

Binary search is commonly useful when:

- The data is sorted.
- We need to search efficiently.
- The search space can be divided into two halves.
- The problem involves finding a boundary or minimum/maximum possible value.
- We want to reduce O(n) search to O(log n).

## Example

Given the sorted array:

[1, 3, 5, 7, 9, 11, 15]

To find 9:

1. Check the middle element 7.
2. 9 is greater than 7, so search the right half.
3. Check 11.
4. 9 is smaller than 11, so search the left half.
5. Find 9.

## Time Complexity

Binary search runs in O(log n) time.

## Space Complexity

An iterative binary search uses O(1) extra space.

A recursive implementation uses O(log n) stack space.

## Common Mistake

Binary search normally requires a sorted search space.

Be careful with the calculation of the middle index and avoid infinite loops when updating the left and right boundaries.

A safe middle calculation is:

mid = left + (right - left) / 2

## Related Problems

Search in Sorted Array, First Occurrence, Last Occurrence, Search Insert Position, Search in Rotated Sorted Array, and Lower Bound.