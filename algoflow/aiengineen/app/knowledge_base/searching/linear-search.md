# Sliding Window Technique

## Concept

The sliding window technique maintains a continuous range of elements using two boundaries, usually called left and right.

Instead of repeatedly processing every possible subarray or substring, the window is expanded or contracted as needed.

## When to Use

Sliding window is commonly useful when:

- We need to work with a contiguous subarray or substring.
- We need the maximum or minimum value for a window.
- We need the longest or shortest range satisfying a condition.
- The problem involves a fixed-size or variable-size window.
- We want to reduce repeated work from O(n²) to O(n).

## Example

Given an array:

[2, 1, 5, 1, 3, 2]

For a fixed window size of 3, the windows are:

[2, 1, 5]
[1, 5, 1]
[5, 1, 3]
[1, 3, 2]

Instead of calculating every sum from scratch, remove the element leaving the window and add the new element entering it.

## Time Complexity

Most sliding window solutions run in O(n) time because each element is usually added and removed at most once.

## Space Complexity

Basic sliding window solutions use O(1) extra space.

Some problems require a HashMap or Set, resulting in O(k) or O(n) additional space.

## Common Mistake

Do not use sliding window for problems that do not involve a contiguous range.

Also distinguish between fixed-size windows and variable-size windows.

## Related Problems

Maximum Sum Subarray of Size K, Longest Substring Without Repeating Characters, Minimum Size Subarray Sum, Longest Repeating Character Replacement, and Minimum Window Substring.