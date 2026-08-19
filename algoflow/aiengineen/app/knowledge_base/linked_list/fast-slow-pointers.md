# Fast and Slow Pointers

## Concept

The fast and slow pointer technique uses two pointers moving through a linked list at different speeds.

The slow pointer usually moves one node at a time while the fast pointer moves two nodes at a time.

## When to Use

Fast and slow pointers are commonly useful when:

- We need to find the middle of a linked list.
- We need to detect a cycle.
- We need to find the starting point of a cycle.
- We need to compare different positions in a linked list.

## Example

For:

1 → 2 → 3 → 4 → 5

Start both pointers at the head.

Slow moves one step.

Fast moves two steps.

When fast reaches the end, slow is around the middle.

The middle node is 3.

## Time Complexity

Most fast and slow pointer solutions run in O(n) time.

## Space Complexity

O(1) extra space.

## Common Mistake

Always check whether fast or fast.next is null before moving fast by two nodes.

Otherwise, a NullPointerException can occur.

## Related Problems

Middle of Linked List, Linked List Cycle, Linked List Cycle II, Palindrome Linked List, and Happy Number.