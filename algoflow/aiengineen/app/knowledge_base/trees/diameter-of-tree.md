# Diameter of Binary Tree

## Concept

The diameter of a binary tree is the length of the longest path between any two nodes.

The path does not have to pass through the root.

If diameter is measured in edges, the diameter through a node can be calculated using the heights of its left and right subtrees.

## When to Use

The diameter technique is commonly useful when:

- We need the longest path between two nodes.
- The problem involves subtree heights.
- We need to combine information from the left and right subtrees.
- The longest path may not pass through the root.

## Example

Consider:

    1
   / \
  2   3
 / \
4   5

The longest path is:

4 → 2 → 1 → 3

The diameter is:

3 edges

## Time Complexity

O(n) using a DFS solution that calculates subtree heights while updating the diameter.

Each node is processed once.

## Space Complexity

O(h) recursive stack space, where h is the tree height.

## Common Mistake

Do not assume that the diameter always passes through the root.

Also check whether the problem measures diameter in edges or nodes.

## Related Problems

Maximum Depth of Binary Tree, Balanced Binary Tree, Longest Path in a Tree, Lowest Common Ancestor, and Path Sum.