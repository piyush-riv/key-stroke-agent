# Activity Selection

## Concept

The Activity Selection problem asks us to select the maximum number of activities that do not overlap.

Each activity has a start time and an end time.

The greedy strategy is to always select the activity that finishes earliest.

## When to Use

Activity selection is commonly useful when:

- We need the maximum number of non-overlapping activities.
- We are scheduling events.
- We need to select intervals without conflicts.
- The problem involves start and finish times.

## Example

Activities:

(1, 3)

(2, 4)

(3, 5)

(5, 7)

Sort activities by finish time.

Choose:

(1, 3)

Then choose:

(3, 5)

Then choose:

(5, 7)

Maximum selected activities:

3

## Algorithm

1. Sort activities by finishing time.
2. Select the first activity.
3. For each remaining activity, check whether its start time is at least the finish time of the last selected activity.
4. If valid, select it.
5. Continue until all activities are processed.

## Time Complexity

O(n log n) because of sorting.

The selection process takes O(n).

## Space Complexity

O(1) extra space if sorting is performed in place, excluding sorting implementation details.

## Common Mistake

Do not select the activity with the earliest start time.

The correct greedy choice is the activity with the earliest finish time.

## Related Problems

Meeting Rooms, Non-overlapping Intervals, Minimum Number of Meeting Rooms, Interval Scheduling, and Maximum Number of Events.