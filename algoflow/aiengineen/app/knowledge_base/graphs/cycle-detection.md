# Graph Cycle Detection

## Concept

A cycle exists in a graph when we can start from a vertex and follow edges to return to that same vertex.

Cycle detection depends on whether the graph is directed or undirected.

DFS can be used to detect cycles in both types of graphs.

## When to Use

Cycle detection is commonly useful when:

- We need to determine whether a graph contains a cycle.
- The problem involves dependencies.
- We need to validate whether a structure is a valid tree.
- We need to detect circular relationships.
- The problem involves directed or undirected graphs.

## Example

An undirected graph:

1 --- 2
|     |
|     |
3 --- 4

The path:

1 → 2 → 4 → 3 → 1

forms a cycle.

## Undirected Graph

During DFS, if we encounter an already visited neighbor that is not the current node's parent, a cycle exists.

## Directed Graph

During DFS, a cycle can be detected by tracking nodes currently in the recursion path.

If we reach a node that is already in the current recursion path, a cycle exists.

## Time Complexity

O(V + E)

where V is the number of vertices and E is the number of edges.

## Space Complexity

O(V) for the visited structure and recursion or auxiliary state.

## Common Mistake

Do not use exactly the same cycle-detection logic for directed and undirected graphs.

For an undirected graph, the parent node must be handled separately.

For a directed graph, track the current recursion path.

## Related Problems

Course Schedule, Course Schedule II, Graph Valid Tree, Redundant Connection, Detect Cycle in Undirected Graph, and Detect Cycle in Directed Graph.