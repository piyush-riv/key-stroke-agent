# Heap Sort

## Concept

Heap sort uses a heap data structure to repeatedly select the largest or smallest element and place it in its correct position.

For ascending order, a max heap is commonly used.

## When to Use

Heap sort is commonly useful when:

- We need guaranteed O(n log n) sorting.
- O(1) auxiliary space is important.
- We need to understand heap operations.
- The problem involves repeatedly selecting the largest or smallest element.

## Example

Given:

[4, 10, 3, 5, 1]

Build a max heap.

The largest element becomes the root.

Move the root to the end and rebuild the heap.

Repeat until the array is sorted:

[1, 3, 4, 5, 10]

## Time Complexity

Best case: O(n log n)

Average case: O(n log n)

Worst case: O(n log n)

## Space Complexity

O(1) extra space for the iterative in-place implementation.

## Common Mistake

Remember that after removing the root, the heap property must be restored.

For ascending order, use a max heap and move the maximum element to the end.

## Related Problems

Priority Queue, Heap, Kth Largest Element, Kth Smallest Element, Merge K Sorted Lists, and Top K Frequent Elements.