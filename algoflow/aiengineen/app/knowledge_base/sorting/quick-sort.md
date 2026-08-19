# Quick Sort

## Concept

Quick sort is a divide-and-conquer sorting algorithm that selects a pivot and partitions the array around it.

Elements smaller than the pivot are placed on one side and larger elements on the other side.

The process is then repeated recursively.

## When to Use

Quick sort is commonly useful when:

- We need an efficient general-purpose sorting algorithm.
- Average-case O(n log n) performance is acceptable.
- In-place sorting is preferred.
- We need to understand partitioning and divide-and-conquer.

## Example

Given:

[6, 3, 8, 2, 5]

Choose 5 as the pivot.

Partition around 5:

[3, 2] 5 [6, 8]

Recursively sort both sides:

[2, 3] 5 [6, 8]

Final result:

[2, 3, 5, 6, 8]

## Time Complexity

Best case: O(n log n)

Average case: O(n log n)

Worst case: O(n²)

## Space Complexity

Average recursive stack space: O(log n).

Worst case recursive stack space: O(n).

## Common Mistake

Poor pivot selection can cause O(n²) performance.

Be careful with the partition boundaries and ensure the recursion reduces the problem size.

## Related Problems

Merge Sort, Heap Sort, Partition Array, Kth Largest Element, and Divide and Conquer.