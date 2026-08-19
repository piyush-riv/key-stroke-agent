# Tree Traversals

## Concept

Tree traversal means visiting every node of a tree in a specific order.

The main binary-tree traversals are preorder, inorder, postorder, and level order.

Preorder visits:

Root → Left → Right

Inorder visits:

Left → Root → Right

Postorder visits:

Left → Right → Root

Level order visits nodes level by level.

## When to Use

Tree traversals are commonly useful when:

- We need to process every tree node.
- We need a specific ordering of nodes.
- We need to evaluate or reconstruct a tree.
- We need breadth-first or depth-first processing.
- The problem explicitly asks for preorder, inorder, postorder, or level order.

## Example

Given:

    1
   / \
  2   3
 / \
4   5

Preorder:

[1, 2, 4, 5, 3]

Inorder:

[4, 2, 5, 1, 3]

Postorder:

[4, 5, 2, 3, 1]

Level order:

[1, 2, 3, 4, 5]

## Time Complexity

O(n), because every node is visited once.

## Space Complexity

DFS recursive traversal uses O(h) stack space.

Level order traversal can use O(n) queue space in the worst case.

## Common Mistake

Remember the exact order of Root, Left, and Right for each traversal.

Inorder is especially important for binary search trees because it produces values in sorted order.

## Related Problems

Binary Tree Inorder Traversal, Binary Tree Preorder Traversal, Binary Tree Postorder Traversal, Binary Tree Level Order Traversal, and Serialize and Deserialize Binary Tree.