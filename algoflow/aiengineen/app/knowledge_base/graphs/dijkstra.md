# Dijkstra's Algorithm

## Concept

Dijkstra's algorithm finds the shortest distance from a source vertex to other vertices in a weighted graph with non-negative edge weights.

It repeatedly selects the unprocessed vertex with the smallest known distance and relaxes its neighboring edges.

A priority queue is commonly used to efficiently select the vertex with the smallest distance.

## When to Use

Dijkstra's algorithm is commonly useful when:

- We need shortest paths in a weighted graph.
- All edge weights are non-negative.
- We need shortest distances from one source.
- The problem involves roads, networks, costs, or distances.
- We need an efficient shortest-path algorithm.

## Example

Consider:

A --1-- B --2-- C

A --5-- C

Start from A.

Initial distances:

A = 0

B = infinity

C = infinity

Process A:

B = 1

C = 5

Process B:

C = min(5, 1 + 2)

C = 3

Final shortest distances:

A = 0

B = 1

C = 3

## Algorithm

1. Set the source distance to 0.
2. Set all other distances to infinity.
3. Put the source into a priority queue.
4. Remove the vertex with the smallest distance.
5. Relax all of its neighboring edges.
6. If a shorter distance is found, update it and add the neighbor to the priority queue.
7. Continue until the priority queue is empty.

## Time Complexity

Using an adjacency list and binary heap priority queue:

O((V + E) log V)

For a sparse graph, this is commonly written as:

O(E log V)

## Space Complexity

O(V + E) for the graph and additional distance and priority queue structures.

## Common Mistake

Dijkstra's algorithm does not correctly handle negative edge weights.

Use Bellman-Ford when negative edge weights may exist.

Also remember that finding the shortest distance is different from finding the actual shortest path. To reconstruct the path, store the previous node for each vertex.

## Related Problems

Network Delay Time, Path With Minimum Effort, Cheapest Flights Within K Stops, Shortest Path, Bellman-Ford, Floyd-Warshall, and Minimum Spanning Tree.