# Topological Sort

## Concept

Topological sorting is an ordering of the vertices of a directed acyclic graph such that for every directed edge u → v, vertex u appears before vertex v.

A graph must be directed and acyclic for a valid topological ordering to exist.

## When to Use

Topological sorting is commonly useful when:

- Tasks have dependencies.
- We need to determine a valid order of operations.
- One task must be completed before another.
- The problem involves prerequisites.
- We need to detect cycles in dependency graphs.

## Example

Suppose:

A → C

B → C

C → D

A valid topological ordering is:

[A, B, C, D]

A and B must appear before C.

C must appear before D.

## Common Approaches

Kahn's algorithm uses indegrees and a queue.

DFS-based topological sorting adds a node to the result after processing all of its neighbors.

If the graph contains a cycle, a complete topological ordering is impossible.

## Time Complexity

O(V + E)

where V is the number of vertices and E is the number of edges.

## Space Complexity

O(V) for indegree, visited state, queue, stack, or result storage.

## Common Mistake

Topological sorting only applies to directed acyclic graphs.

If the graph contains a cycle, there is no valid topological ordering.

For Kahn's algorithm, if fewer than V vertices are processed, the graph contains a cycle.

## Related Problems

Course Schedule, Course Schedule II, Alien Dictionary, Task Scheduling, Dependency Resolution, and Build Systems.