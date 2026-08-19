# Selection Sort

## Concept

Selection sort repeatedly finds the smallest element from the unsorted portion of the array and places it at the beginning of that portion.

## When to Use

Selection sort is commonly useful when:

- Learning sorting algorithms.
- The input size is small.
- We want a simple in-place sorting algorithm.
- The number of swaps should be minimized.

## Example

Given:

[5, 3, 8, 1]

Find the smallest element, 1, and place it at the beginning:

[1, 3, 8, 5]

Then find the smallest element in the remaining portion:

[1, 3, 8, 5]

Continue until the array is sorted:

[1, 3, 5, 8]

## Time Complexity

Best case: O(n²)

Average case: O(n²)

Worst case: O(n²)

## Space Complexity

O(1) extra space.

Selection sort is an in-place sorting algorithm.

## Common Mistake

Confusing the current index with the index of the minimum element.

The algorithm must first find the minimum element in the unsorted portion before swapping.

## Related Problems

Bubble Sort, Insertion Sort, Merge Sort, Quick Sort, and Heap Sort.