# Subsets

## Concept

The Subsets problem asks us to generate every possible subset of a given array.

For an array containing n distinct elements, there are 2^n possible subsets.

Each element has two choices:

Include it.

Exclude it.

## When to Use

The subsets pattern is commonly useful when:

- We need all possible subsets.
- Each element can be selected or skipped.
- The problem involves include/exclude decisions.
- We need to generate combinations.

## Example

Given:

[1, 2, 3]

The subsets include:

[]

[1]

[2]

[3]

[1, 2]

[1, 3]

[2, 3]

[1, 2, 3]

Total subsets:

2^3 = 8

## Algorithm

At each index:

1. Include the current element.
2. Recursively process the remaining elements.
3. Remove the current element.
4. Exclude the current element.
5. Continue recursively.

## Time Complexity

O(n * 2^n) when accounting for copying each subset into the result.

There are 2^n subsets.

## Space Complexity

O(n) recursion depth excluding the output.

The output itself requires O(n * 2^n) space.

## Common Mistake

Do not forget to remove the selected element when returning from the recursive call.

## Related Problems

Subsets II, Combination Sum, Permutations, Letter Combinations of a Phone Number, and Partition Problems.