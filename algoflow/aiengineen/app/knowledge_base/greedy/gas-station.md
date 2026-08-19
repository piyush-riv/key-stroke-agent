# Gas Station

## Concept

The Gas Station problem asks us to find a starting station from which a vehicle can complete a circular route.

Each station provides a certain amount of gas and requires a certain amount of gas to travel to the next station.

The greedy solution uses the total gas balance and the current running balance.

## When to Use

The greedy approach is commonly useful when:

- The route is circular.
- Each position provides resources and has a cost.
- We need to find a valid starting position.
- We need to determine whether completing the entire route is possible.

## Example

Gas:

[1, 2, 3, 4, 5]

Cost:

[3, 4, 5, 1, 2]

The total gas is equal to the total cost.

A valid starting station is:

3

## Algorithm

1. Calculate total gas minus total cost.
2. If the total is negative, completing the circuit is impossible.
3. Maintain the current balance.
4. If the current balance becomes negative, the current starting point cannot work.
5. Set the next station as the new starting point.
6. Continue through the array.

## Time Complexity

O(n).

## Space Complexity

O(1) extra space.

## Common Mistake

Do not restart from every station.

If the current balance becomes negative while traveling from a starting point, none of the stations between that starting point and the failure point can be a valid start.

## Related Problems

Jump Game, Circular Array, Minimum Refueling Stops, and Route Scheduling.