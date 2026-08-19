# Linked List Basics

## Concept

A linked list is a linear data structure where elements are stored in nodes.

Each node contains data and a reference to the next node.

Unlike arrays, linked-list elements are not required to be stored in contiguous memory.

## When to Use

Linked lists are commonly useful when:

- Frequent insertion and deletion are required.
- The size of the data changes dynamically.
- We need to insert elements without shifting other elements.
- The problem involves nodes and references.

## Example

A singly linked list can look like:

10 → 20 → 30 → null

Each node stores a value and a reference to the next node.

The first node is called the head.

## Time Complexity

Accessing an element by index takes O(n).

Searching takes O(n).

Insertion or deletion at the beginning takes O(1).

Insertion or deletion after a known node can take O(1).

## Space Complexity

A linked list uses O(n) space for n nodes.

## Common Mistake

Do not try to access linked-list elements using array-style indexing.

Be careful not to lose the reference to the next node when changing links.

## Related Problems

Reverse Linked List, Linked List Cycle, Merge Two Sorted Lists, Remove Nth Node, Middle of Linked List, and Palindrome Linked List.