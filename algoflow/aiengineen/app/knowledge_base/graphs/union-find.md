# Union Find

## Concept

Union-Find, also called Disjoint Set Union or DSU, is a data structure used to maintain multiple disjoint sets.

It efficiently supports two main operations:

Find determines which set an element belongs to.

Union combines two sets into one set.

Path compression and union by rank or size make these operations very efficient.

## When to Use

Union-Find is commonly useful when:

- We need to determine whether two nodes belong to the same group.
- We need to merge connected components.
- We need to detect cycles in an undirected graph.
- The problem involves dynamic connectivity.
- We need to build a Minimum Spanning Tree using Kruskal's algorithm.

## Example

Initially:

{1} {2} {3} {4}

Union(1, 2):

{1, 2} {3} {4}

Union(2, 3):

{1, 2, 3} {4}

Now:

Find(1) and Find(3)

return the same representative.

Therefore, 1 and 3 belong to the same set.

## Main Operations

Find(x) returns the representative of the set containing x.

Union(x, y) combines the sets containing x and y.

Path compression makes Find faster by directly connecting nodes to the set representative.

Union by rank or size keeps the trees shallow.

## Time Complexity

With path compression and union by rank or size:

Amortized time per operation is approximately O(alpha(n)).

alpha(n) is the inverse Ackermann function and grows extremely slowly.

For practical input sizes, it is effectively close to O(1).

## Space Complexity

O(n) for parent and rank or size arrays.

## Common Mistake

Do not compare node values directly to determine whether they belong to the same set.

Use Find(x) and Find(y).

Also make sure to perform Union only when the two elements belong to different sets.

## Related Problems

Number of Connected Components, Redundant Connection, Graph Valid Tree, Accounts Merge, Kruskal's Algorithm, and Number of Provinces.