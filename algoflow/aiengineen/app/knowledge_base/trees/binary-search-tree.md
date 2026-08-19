# Binary Search Tree

## Concept

A binary search tree, or BST, is a binary tree where values in the left subtree are smaller than the node value and values in the right subtree are larger.

This ordering allows efficient searching when the tree is balanced.

## When to Use

Binary search trees are commonly useful when:

- We need ordered data.
- We need efficient search, insertion, and deletion.
- We need to maintain elements in sorted order.
- We need to find minimum or maximum values.
- The problem involves predecessor or successor operations.

## Example

A BST can look like:

    5
   / \
  3   8
 / \   \
2   4   10

Values smaller than 5 are in its left subtree.

Values larger than 5 are in its right subtree.

Inorder traversal gives:

[2, 3, 4, 5, 8, 10]

## Time Complexity

For a balanced BST:

Search: O(log n)

Insertion: O(log n)

Deletion: O(log n)

For a highly unbalanced BST, these operations can become O(n).

## Space Complexity

O(n) for storing n nodes.

Recursive operations use O(h) stack space.

## Common Mistake

Do not assume every BST operation is O(log n).

The tree must be reasonably balanced for logarithmic performance.

Also remember that inorder traversal of a valid BST produces sorted values.

## Related Problems

Search in a Binary Search Tree, Insert into a Binary Search Tree, Delete Node in a BST, Validate Binary Search Tree, Kth Smallest Element in a BST, and Lowest Common Ancestor of a BST.