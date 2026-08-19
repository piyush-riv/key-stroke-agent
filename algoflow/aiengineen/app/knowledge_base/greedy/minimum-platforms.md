# Minimum Platforms

## Concept

The Minimum Platforms problem asks for the minimum number of railway platforms required so that no train has to wait.

Each train has an arrival time and a departure time.

The goal is to find the maximum number of trains present at the station at the same time.

That maximum number is the minimum number of platforms required.

## When to Use

This greedy technique is commonly useful when:

- We need to find the minimum resources required for overlapping intervals.
- The problem involves arrival and departure times.
- Multiple events can overlap.
- We need to determine the maximum number of simultaneous activities.

## Example

Arrival times:

[900, 940, 950, 1100, 1500, 1800]

Departure times:

[910, 1200, 1120, 1130, 1900, 2000]

Sort both arrays.

Compare the next arrival with the next departure.

If an arrival occurs before or at the departure, another platform is required.

If a departure occurs first, a platform becomes available.

The maximum number of platforms needed is the answer.

## Algorithm

1. Sort all arrival times.
2. Sort all departure times.
3. Use two pointers for the arrival and departure arrays.
4. If the next arrival occurs before or at the next departure, increase the platform count.
5. Otherwise, decrease the platform count because a train has departed.
6. Track the maximum platform count reached.

## Time Complexity

O(n log n) because both arrays must be sorted.

The two-pointer traversal takes O(n).

## Space Complexity

O(1) extra space if the input arrays can be sorted in place.

## Common Mistake

Be careful when an arrival time equals a departure time.

Depending on the problem definition, if a train arrives at the same time another train departs, both may require a platform.

For the common railway-platform formulation, arrival <= departure means another platform is required.

## Related Problems

Meeting Rooms II, Activity Selection, Merge Intervals, Minimum Number of Meeting Rooms, Interval Scheduling, and Minimum Arrows to Burst Balloons.