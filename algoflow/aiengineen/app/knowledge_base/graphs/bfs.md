# Breadth First Search

## Concept

Breadth First Search, or BFS, is a graph traversal algorithm that explores nodes level by level.

BFS uses a queue to process nodes in the order they are discovered.

It is commonly used to find the shortest path in an unweighted graph.

## When to Use

BFS is commonly useful when:

- We need level-by-level traversal.
- We need the shortest path in an unweighted graph.
- We need to find the minimum number of moves or steps.
- The problem involves exploring nearby nodes first.
- We need level-order traversal of a tree.

## Example

Given:

1 --- 2 --- 4
|
3

Starting from 1:

Visit 1.

Then visit its neighbors:

2, 3

Then visit:

4

Traversal order:

[1, 2, 3, 4]

## Algorithm

1. Put the starting node into a queue.
2. Mark it as visited.
3. Remove a node from the queue.
4. Process the node.
5. Add its unvisited neighbors to the queue.
6. Repeat until the queue is empty.

## Time Complexity

O(V + E)

where V is the number of vertices and E is the number of edges.

## Space Complexity

O(V) for the queue and visited structure in the worst case.

## Common Mistake

Do not mark a node as visited only after removing it from the queue.

Mark it when adding it to the queue to avoid adding the same node multiple times.

Also remember that BFS gives shortest distance in an unweighted graph, not necessarily in a weighted graph.

## Related Problems

Binary Tree Level Order Traversal, Number of Islands, Rotting Oranges, Shortest Path in Binary Matrix, Word Ladder, and Clone Graph.