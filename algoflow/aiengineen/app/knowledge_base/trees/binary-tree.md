# Binary Tree

## Concept

A binary tree is a tree data structure where each node has at most two children.

The two children are usually called the left child and the right child.

A binary tree does not require the values to be ordered.

## When to Use

Binary trees are commonly useful when:

- Each node can have at most two children.
- The problem involves hierarchical data.
- We need recursive tree traversal.
- We need to represent decision structures.
- The problem involves paths, subtrees, depth, or height.

## Example

A binary tree can look like:

    1
   / \
  2   3
 / \
4   5

Node 1 is the root.

Nodes 2 and 3 are children of 1.

Nodes 4 and 5 are children of 2.

Nodes 3, 4, and 5 are leaf nodes.

## Important Properties

A binary tree can have at most two children per node.

A tree with n nodes has n - 1 edges when it is non-empty.

The maximum number of nodes at level k is 2^k when the root is at level 0.

A binary tree can be balanced, complete, full, perfect, or skewed depending on its structure.

## Common Types

A full binary tree is a tree where every node has either zero or two children.

A complete binary tree has all levels completely filled except possibly the last, and the last level is filled from left to right.

A perfect binary tree has every internal node with two children and all leaf nodes at the same level.

A skewed binary tree has nodes mostly extending in one direction.

## Time Complexity

Traversing all nodes takes O(n) time.

Searching an arbitrary binary tree takes O(n) time in the worst case.

## Space Complexity

O(n) space is required to store n nodes.

Recursive tree operations use O(h) call-stack space, where h is the height of the tree.

## Common Mistake

Do not confuse a binary tree with a binary search tree.

A binary tree only restricts the number of children to two.

A binary search tree additionally follows an ordering rule where smaller values are placed on the left and larger values on the right.

## Related Problems

Binary Tree Traversals, Maximum Depth of Binary Tree, Same Tree, Invert Binary Tree, Symmetric Tree, Diameter of Binary Tree, Lowest Common Ancestor, and Path Sum.