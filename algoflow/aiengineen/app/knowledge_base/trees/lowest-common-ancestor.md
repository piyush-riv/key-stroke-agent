# Lowest Common Ancestor

## Concept

The lowest common ancestor, or LCA, of two nodes is the deepest node that is an ancestor of both nodes.

An ancestor can be a node itself or any node above it in the tree.

## When to Use

Lowest common ancestor techniques are commonly useful when:

- We need the closest shared ancestor of two nodes.
- The problem involves relationships between nodes.
- We need to find paths between two nodes.
- The tree is a binary tree or binary search tree.

## Example

Given:

    3
   / \
  5   1
 / \ / \
6  2 0  8

The lowest common ancestor of 6 and 2 is:

5

The lowest common ancestor of 6 and 1 is:

3

## Time Complexity

A typical binary-tree LCA solution takes O(n) time.

For a BST, the ordering property can allow an O(h) solution.

## Space Complexity

O(h) recursive stack space for a recursive solution.

For a balanced tree, this is O(log n).

For a skewed tree, this can become O(n).

## Common Mistake

Do not confuse the lowest common ancestor with the root.

The LCA must be the deepest node that is an ancestor of both target nodes.

For a BST, use the ordering property to decide whether to move left or right.

## Related Problems

Lowest Common Ancestor of a Binary Tree, Lowest Common Ancestor of a BST, Binary Tree Paths, Distance Between Nodes, and Kth Ancestor of a Tree.