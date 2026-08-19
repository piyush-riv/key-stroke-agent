# Depth First Search

## Concept

Depth First Search, or DFS, is a graph traversal algorithm that explores as far as possible along one path before backtracking.

DFS can be implemented using recursion or an explicit stack.

## When to Use

DFS is commonly useful when:

- We need to explore connected components.
- We need to search deeply before exploring other branches.
- The problem involves backtracking.
- We need to detect cycles.
- We need to explore paths in a graph or tree.

## Example

Given:

1 --- 2 --- 4
|
3

Starting from 1, one possible DFS order is:

[1, 2, 4, 3]

The exact order can depend on the order of neighbors.

## Algorithm

Recursive DFS:

1. Mark the current node as visited.
2. Process the node.
3. Recursively visit each unvisited neighbor.

Iterative DFS:

1. Push the starting node onto a stack.
2. Pop a node.
3. Process it if it has not been visited.
4. Push its unvisited neighbors.
5. Repeat until the stack is empty.

## Time Complexity

O(V + E)

where V is the number of vertices and E is the number of edges.

## Space Complexity

O(V) in the worst case for the visited structure and recursion stack or explicit stack.

## Common Mistake

Always track visited nodes in graphs that may contain cycles.

For recursive DFS, make sure the base conditions prevent infinite recursion.

## Related Problems

Number of Islands, Number of Connected Components, Path Sum, Clone Graph, Course Schedule, Cycle Detection, and Backtracking.