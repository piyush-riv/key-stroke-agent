# Insertion Sort

## Concept

Insertion sort builds the sorted portion of an array one element at a time.

Each new element is inserted into its correct position among the elements that are already sorted.

## When to Use

Insertion sort is commonly useful when:

- The array is small.
- The data is nearly sorted.
- We need a simple in-place sorting algorithm.
- We need a stable sorting algorithm.

## Example

Given:

[5, 3, 4, 1]

Start with 5 as the sorted portion.

Insert 3:

[3, 5, 4, 1]

Insert 4:

[3, 4, 5, 1]

Insert 1:

[1, 3, 4, 5]

## Time Complexity

Best case: O(n) when the array is already sorted.

Average case: O(n²)

Worst case: O(n²)

## Space Complexity

O(1) extra space.

## Common Mistake

Do not overwrite the element being inserted before saving its value.

Shift larger elements to the right and then place the saved element in its correct position.

## Related Problems

Bubble Sort, Selection Sort, Merge Sort, Quick Sort, and Heap Sort.