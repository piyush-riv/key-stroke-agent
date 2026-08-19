# Next Greater Element

## Concept

The next greater element of an element is the first element to its right that is greater than it.

A monotonic stack can solve many next-greater-element problems efficiently.

## When to Use

Next greater element techniques are commonly useful when:

- We need the first greater value to the right.
- We need to process elements looking toward the future.
- A brute-force nested loop would take O(n²).
- The problem involves nearest greater or smaller elements.

## Example

Given:

[4, 5, 2, 10]

The next greater elements are:

4 → 5

5 → 10

2 → 10

10 → -1

## Time Complexity

A monotonic stack solution usually runs in O(n) time because each element is pushed and popped at most once.

## Space Complexity

O(n) in the worst case for the stack.

## Common Mistake

Do not pop an element from the stack unless the current element satisfies the required greater-element condition.

Be careful about whether the problem asks for the next greater element on the right or left.

## Related Problems

Daily Temperatures, Next Greater Element I, Next Greater Element II, Stock Span, Largest Rectangle in Histogram, and Previous Greater Element.