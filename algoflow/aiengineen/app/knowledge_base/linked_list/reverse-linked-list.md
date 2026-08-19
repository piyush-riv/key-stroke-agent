# Reverse Linked List

## Concept

Reversing a linked list means changing the direction of every node's next reference.

For example:

1 → 2 → 3 → null

becomes:

3 → 2 → 1 → null

## When to Use

Reversing a linked list is commonly useful when:

- The problem asks to reverse all nodes.
- We need to process a linked list from the opposite direction.
- A linked-list problem requires changing node references.
- We need to understand pointer manipulation.

## Example

Maintain three references:

prev, current, and next.

For:

1 → 2 → 3

Change:

1 → null

then:

2 → 1

then:

3 → 2 → 1

The new head is 3.

## Time Complexity

O(n), because every node is processed once.

## Space Complexity

O(1) extra space for the iterative approach.

## Common Mistake

Save the next node before changing current.next.

Otherwise, the remaining part of the linked list can be lost.

## Related Problems

Reverse Linked List II, Palindrome Linked List, Reorder List, Reverse Nodes in K-Group, and Swap Nodes in Pairs.