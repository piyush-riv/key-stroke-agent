# Tree Height and Depth

## Concept

The depth of a node is the number of edges from the root to that node.

The height of a node is the number of edges on the longest path from that node to a leaf.

The height of a tree is the height of its root.

## When to Use

Height and depth are commonly useful when:

- We need the maximum depth of a binary tree.
- We need to calculate tree height.
- We need to determine whether a tree is balanced.
- We need to compare distances between nodes and the root.
- The problem involves levels or paths in a tree.

## Example

Consider:

    1
   / \
  2   3
 /
4

Depth of node 1:

0

Depth of node 2:

1

Depth of node 4:

2

The height of the tree is:

2

## Time Complexity

Calculating the height using DFS takes O(n).

Every node is visited once.

## Space Complexity

O(h) recursive stack space for DFS, where h is the tree height.

For a balanced tree, this is O(log n).

For a completely skewed tree, this can become O(n).

## Common Mistake

Be careful about whether the problem defines height using edges or nodes.

Some problems define the height of a single-node tree as 0, while others count nodes and return 1.

## Related Problems

Maximum Depth of Binary Tree, Minimum Depth of Binary Tree, Balanced Binary Tree, Diameter of Binary Tree, and Binary Tree Level Order Traversal.