# Permutations

## Concept

A permutation is an arrangement of elements in a specific order.

For n distinct elements, there are n! possible permutations.

Backtracking can generate all possible arrangements.

## When to Use

The permutation pattern is commonly useful when:

- Order matters.
- We need every possible arrangement.
- We need to arrange elements without repetition.
- The problem involves choosing one unused element at each step.

## Example

Given:

[1, 2, 3]

Some permutations are:

[1, 2, 3]

[1, 3, 2]

[2, 1, 3]

[2, 3, 1]

[3, 1, 2]

[3, 2, 1]

Total:

3! = 6

## Algorithm

1. Maintain the current permutation.
2. Choose an unused element.
3. Add it to the current permutation.
4. Recursively continue.
5. Remove the element when returning.
6. Try another unused element.

## Time Complexity

O(n * n!).

There are n! permutations and each complete permutation takes O(n) time to construct or copy.

## Space Complexity

O(n) recursion depth excluding the output.

The output requires O(n * n!) space.

## Common Mistake

Do not confuse subsets with permutations.

In subsets, order does not matter.

In permutations, order matters.

## Related Problems

Permutations II, Next Permutation, Combination Problems, Letter Combinations, and N-Queens.