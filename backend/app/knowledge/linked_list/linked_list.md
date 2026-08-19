# Fast and Slow Pointer

## Concept

The fast and slow pointer technique uses two pointers that move through a linked list at different speeds.

The slow pointer usually moves one node at a time, while the fast pointer moves two nodes at a time.

## When to Use

This technique is useful for:

- Detecting cycles.
- Finding the middle of a linked list.
- Finding the starting point of a cycle.
- Solving problems involving relative positions in a linked list.

## Example

To find the middle of a linked list, move slow by one node and fast by two nodes.

When fast reaches the end, slow will be approximately at the middle.

## Time Complexity

Most fast and slow pointer solutions run in O(n) time.

## Space Complexity

The technique normally uses O(1) extra space.

## Common Mistake

When checking a linked list cycle, make sure to check that fast and fast.next are not None before moving the pointers.