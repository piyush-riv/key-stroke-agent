# Linked List Cycle Detection

## Concept

A cycle exists in a linked list when a node points back to a previous node instead of eventually pointing to null.

Floyd's Cycle Detection Algorithm uses slow and fast pointers to detect such a cycle.

## When to Use

Cycle detection is commonly useful when:

- A linked list may contain a loop.
- We need to determine whether traversal can reach null.
- The problem involves repeated states or positions.
- Extra space should be avoided.

## Example

Consider:

1 → 2 → 3 → 4
        ↑     ↓
        ← ← ←

The nodes form a cycle.

Slow moves one step and fast moves two steps.

If a cycle exists, they will eventually meet.

## Time Complexity

O(n) time.

## Space Complexity

O(1) extra space.

## Common Mistake

Do not move fast without first checking that fast and fast.next are not null.

Also remember that the pointers meeting proves a cycle exists, but the meeting point is not necessarily the cycle's starting node.

## Related Problems

Linked List Cycle, Linked List Cycle II, Find Middle of Linked List, Happy Number, and Circular Array Loop.