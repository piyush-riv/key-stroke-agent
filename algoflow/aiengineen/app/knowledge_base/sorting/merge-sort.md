# Merge Sort

## Concept

Merge sort is a divide-and-conquer sorting algorithm.

It divides the array into smaller halves, recursively sorts each half, and then merges the sorted halves.

## When to Use

Merge sort is commonly useful when:

- We need guaranteed O(n log n) sorting.
- Stable sorting is required.
- The input is large.
- We are learning divide-and-conquer.
- We need to sort linked lists efficiently.

## Example

Given:

[8, 3, 5, 1]

Divide:

[8, 3] [5, 1]

Divide again:

[8] [3] [5] [1]

Merge sorted parts:

[3, 8] [1, 5]

Final merge:

[1, 3, 5, 8]

## Time Complexity

Best case: O(n log n)

Average case: O(n log n)

Worst case: O(n log n)

## Space Complexity

O(n) extra space for the temporary arrays used during merging.

## Common Mistake

Be careful when merging the two sorted halves.

Always compare the current elements from both halves and copy the smaller one.

## Related Problems

Quick Sort, Heap Sort, Divide and Conquer, Count Inversions, and Merge Two Sorted Arrays.