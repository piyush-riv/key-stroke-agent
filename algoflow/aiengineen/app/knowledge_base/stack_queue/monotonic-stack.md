# Monotonic Stack

## Concept

A monotonic stack is a stack that maintains its elements in increasing or decreasing order.

Elements are removed from the stack when they violate the required ordering.

## When to Use

Monotonic stacks are commonly useful when:

- We need the next greater element.
- We need the next smaller element.
- We need the previous greater or smaller element.
- We need the nearest element satisfying a condition.
- A brute-force solution would require comparing many pairs.

## Example

Given:

[2, 1, 5, 3]

For finding the next greater element, maintain a decreasing stack.

When 5 is encountered, remove smaller elements that have found their next greater value.

## Time Complexity

Most monotonic stack solutions run in O(n) time because each element is pushed and popped at most once.

## Space Complexity

O(n) in the worst case.

## Common Mistake

Choose the correct increasing or decreasing stack based on whether the problem asks for greater or smaller elements.

Do not remove elements without understanding what condition they represent.

## Related Problems

Next Greater Element, Daily Temperatures, Stock Span, Largest Rectangle in Histogram, Trapping Rain Water, and Next Smaller Element.