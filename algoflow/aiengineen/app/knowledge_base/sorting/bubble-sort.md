# Bubble Sort

## Concept

Bubble sort repeatedly compares adjacent elements and swaps them if they are in the wrong order.

After each pass, the largest unsorted element moves to its correct position.

## When to Use

Bubble sort is commonly useful when:

- Learning basic sorting concepts.
- The input size is very small.
- We need a simple sorting algorithm.
- The problem specifically asks for bubble sort.

## Example

Given:

[5, 3, 8, 1]

Compare adjacent elements and swap when necessary.

After the first pass:

[3, 5, 1, 8]

The largest element, 8, has reached the end.

Continue until the array is sorted:

[1, 3, 5, 8]

## Time Complexity

Best case: O(n) when the array is already sorted and an optimization detects no swaps.

Average case: O(n²)

Worst case: O(n²)

## Space Complexity

O(1) extra space.

Bubble sort is an in-place sorting algorithm.

## Common Mistake

Forgetting to reduce the unsorted portion after every pass.

Also, bubble sort is usually inefficient for large inputs.

## Related Problems

Selection Sort, Insertion Sort, Merge Sort, Quick Sort, and Heap Sort.