# N-Queens

## Concept

The N-Queens problem asks us to place N queens on an N × N chessboard so that no two queens attack each other.

No two queens can share the same row, column, or diagonal.

Backtracking tries placing a queen row by row and removes it when the placement leads to an invalid configuration.

## When to Use

N-Queens is commonly useful when:

- We need to place objects under multiple constraints.
- A decision can be made one row or position at a time.
- Invalid configurations can be rejected early.
- The problem requires generating valid arrangements.

## Example

For N = 4, one valid arrangement is:

. Q . .

. . . Q

Q . . .

. . Q .

Each row and column contains exactly one queen.

No two queens share a diagonal.

## Algorithm

1. Start from the first row.
2. Try placing a queen in each column.
3. Check whether the position is safe.
4. If safe, place the queen.
5. Recursively process the next row.
6. If no valid position exists, remove the queen.
7. Try the next column.
8. Continue until all N queens are placed.

## Time Complexity

The worst-case time complexity is approximately O(N!).

Pruning invalid positions makes practical execution faster.

## Space Complexity

O(N) recursion depth and O(N²) space for the board representation.

The space can be reduced using sets or arrays to track occupied columns and diagonals.

## Common Mistake

Checking only the same column is not enough.

A queen can also attack diagonally.

For a position (row, column), track both diagonal directions.

## Related Problems

Sudoku Solver, Graph Coloring, Permutations, Combinations, Word Search, and Constraint Satisfaction Problems.