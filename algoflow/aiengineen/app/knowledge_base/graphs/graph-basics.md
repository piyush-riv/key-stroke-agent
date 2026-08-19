# Graph Basics

## Concept

A graph is a data structure made of vertices, also called nodes, and edges that connect pairs of vertices.

Graphs can be directed or undirected.

In a directed graph, edges have a direction.

In an undirected graph, edges do not have a direction.

Graphs can also be weighted or unweighted.

## When to Use

Graphs are commonly useful when:

- We need to represent relationships between objects.
- The problem involves connections or networks.
- We need to find paths between nodes.
- The data is not naturally hierarchical.
- The problem involves dependencies or routes.

## Example

An undirected graph can look like:

1 --- 2
|     |
|     |
3 --- 4

The vertices are:

[1, 2, 3, 4]

The edges connect the vertices.

For example:

1 is connected to 2 and 3.

## Common Representations

An adjacency matrix stores connections in a two-dimensional array.

An adjacency list stores the neighbors of each vertex.

For sparse graphs, adjacency lists are usually more space-efficient.

## Time Complexity

With an adjacency list:

Adding a vertex is typically O(1).

Checking all neighbors of a vertex takes O(degree of vertex).

Traversing the entire graph using BFS or DFS takes O(V + E), where V is the number of vertices and E is the number of edges.

## Space Complexity

An adjacency list requires O(V + E) space.

An adjacency matrix requires O(V²) space.

## Common Mistake

Do not assume every graph is connected.

A graph can contain multiple disconnected components.

Also remember to track visited nodes during traversal to avoid processing the same node repeatedly.

## Related Problems

Breadth First Search, Depth First Search, Number of Islands, Clone Graph, Course Schedule, Shortest Path, and Minimum Spanning Tree.