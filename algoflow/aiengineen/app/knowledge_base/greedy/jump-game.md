# Jump Game

## Concept

The Jump Game asks whether we can reach the last index of an array.

Each value represents the maximum number of positions we can jump forward from that index.

A greedy solution keeps track of the farthest position that can currently be reached.

## When to Use

The greedy approach is commonly useful when:

- Each array element represents a maximum jump length.
- We need to determine whether the final position is reachable.
- We need to maximize the reachable position.
- A dynamic programming solution can be optimized using a running maximum.

## Example

Given:

[2, 3, 1, 1, 4]

Start at index 0.

The maximum reachable position becomes:

2

From index 1, we can reach:

4

Therefore, the last index is reachable.

Result:

true

## Algorithm

1. Maintain the farthest reachable index.
2. Traverse the array.
3. If the current index is greater than the farthest reachable index, it cannot be reached.
4. Update the farthest reachable index using the current jump length.
5. If the farthest position reaches the last index, return true.

## Time Complexity

O(n).

Each element is processed once.

## Space Complexity

O(1) extra space.

## Common Mistake

Do not simply check whether the current element is large.

The important value is the farthest index reachable from all positions processed so far.

## Related Problems

Jump Game II, Gas Station, Can Place Flowers, Reach a Number, and Minimum Jumps.