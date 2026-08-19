# Queue

## Concept

A queue is a linear data structure that follows the FIFO principle: First In, First Out.

The element inserted first is removed first.

The main operations are enqueue and dequeue.

## When to Use

Queues are commonly useful when:

- We need FIFO behavior.
- We process elements in the order they arrive.
- We need BFS traversal.
- We need scheduling or task processing.
- We need to simulate waiting lines.

## Example

Insert:

1 → 2 → 3

The front element is 1.

Remove 1 first.

Then 2 becomes the front.

## Time Complexity

Enqueue: O(1)

Dequeue: O(1)

Peek: O(1)

## Space Complexity

O(n) for n stored elements.

## Common Mistake

Do not remove elements inefficiently from the beginning of an array-based structure.

In Java, use a suitable queue implementation such as ArrayDeque.

## Related Problems

Binary Tree Level Order Traversal, Breadth First Search, Number of Islands, Rotting Oranges, Sliding Window Maximum, and Task Scheduling.