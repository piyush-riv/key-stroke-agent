# Binary Search

## Concept

Binary search is a searching algorithm that repeatedly divides a sorted search space into two halves.

It compares the target with the middle element and eliminates half of the remaining search space.

## When to Use

Binary search is useful when:

- The data is sorted.
- We can determine whether the answer is to the left or right of the middle.
- The search space can be repeatedly divided.

## Algorithm

Set left to the beginning of the search range.

Set right to the end of the search range.

Calculate the middle position.

If the middle value equals the target, return the position.

If the middle value is smaller than the target, search the right half.

Otherwise, search the left half.

## Time Complexity

Binary search runs in O(log n) time.

## Space Complexity

An iterative binary search uses O(1) extra space.

## Common Mistakes

A common mistake is using binary search on data that does not satisfy the required ordering or search-space condition.

Another common mistake is calculating the middle index incorrectly or updating the left and right boundaries incorrectly.