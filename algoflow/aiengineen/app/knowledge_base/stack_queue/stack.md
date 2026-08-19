# Stack

## Concept

A stack is a linear data structure that follows the LIFO principle: Last In, First Out.

The element inserted last is removed first.

The main operations are push, pop, and peek.

## When to Use

Stacks are commonly useful when:

- We need LIFO behavior.
- We need to reverse or process elements in reverse order.
- We need to match opening and closing brackets.
- We need to process nested structures.
- We need to implement DFS iteratively.

## Example

Push:

1 → 2 → 3

The top element is 3.

Pop removes:

3

Then 2 becomes the top.

## Time Complexity

Push: O(1)

Pop: O(1)

Peek: O(1)

## Space Complexity

O(n) for n stored elements.

## Common Mistake

Do not call pop or peek on an empty stack.

Always check whether the stack contains an element before accessing its top.

## Related Problems

Valid Parentheses, Min Stack, Next Greater Element, Daily Temperatures, Evaluate Reverse Polish Notation, and DFS.