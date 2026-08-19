# Sudoku Solver

## Concept

Sudoku Solver is a backtracking problem where we fill an incomplete 9 × 9 Sudoku board while satisfying all Sudoku constraints.

Each row must contain digits 1 through 9 without repetition.

Each column must contain digits 1 through 9 without repetition.

Each 3 × 3 subgrid must contain digits 1 through 9 without repetition.

## When to Use

Sudoku backtracking is commonly useful when:

- We need to fill a grid while satisfying multiple constraints.
- A choice can be tested and undone.
- The problem requires exploring possible configurations.
- Invalid partial solutions can be rejected early.

## Example

For an empty cell:

1. Try a digit from 1 to 9.
2. Check whether the digit is valid in the row.
3. Check whether it is valid in the column.
4. Check whether it is valid in the 3 × 3 subgrid.
5. Place the digit.
6. Recursively solve the remaining board.
7. If the solution fails, remove the digit and try another.

## Algorithm

1. Find an empty cell.
2. Try every digit from 1 to 9.
3. Check whether the digit is valid.
4. Place the digit.
5. Recursively solve the remaining cells.
6. If no solution is possible, undo the placement.
7. Continue until the board is completely filled.

## Time Complexity

The worst-case time complexity is exponential because many possible assignments may need to be explored.

For a standard 9 × 9 Sudoku, the search space is bounded by a finite number of possible configurations.

## Space Complexity

O(1) auxiliary board space for a fixed 9 × 9 board, excluding recursion stack.

The recursion depth is at most the number of empty cells.

## Common Mistake

Always validate the row, column, and 3 × 3 subgrid before placing a digit.

Do not forget to undo the placement when backtracking.

## Related Problems

N-Queens, Word Search, Combination Sum, Graph Coloring, and Constraint Satisfaction Problems.