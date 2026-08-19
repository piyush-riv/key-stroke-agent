# Combinations

## Concept

A combination is a selection of elements where order does not matter.

For example, choosing [1, 2] is the same combination as choosing [2, 1].

Backtracking can generate all combinations by choosing elements from a starting index.

## When to Use

Combinations are commonly useful when:

- We need to choose exactly k elements.
- Order does not matter.
- We need to generate all possible selections.
- The problem involves choosing or excluding elements.

## Example

Given:

[1, 2, 3, 4]

Choose 2 elements.

The combinations are:

[1, 2]

[1, 3]

[1, 4]

[2, 3]

[2, 4]

[3, 4]

The total number is:

C(4, 2) = 6

## Algorithm

1. Start from a given index.
2. Choose an element.
3. Add it to the current combination.
4. Recursively choose the remaining elements.
5. Remove the selected element when returning.
6. Continue from the next index.

## Time Complexity

For generating all k-element combinations:

O(C(n, k) * k)

because there are C(n, k) combinations and each result contains k elements.

## Space Complexity

O(k) recursion depth excluding the output.

The output requires O(C(n, k) * k) space.

## Common Mistake

Do not treat combinations like permutations.

In combinations, order does not matter.

Use a starting index so that previously selected elements are not reused and duplicate orderings are avoided.

## Related Problems

Combination Sum, Combination Sum II, Subsets, Permutations, Letter Combinations of a Phone Number, and N-Queens.