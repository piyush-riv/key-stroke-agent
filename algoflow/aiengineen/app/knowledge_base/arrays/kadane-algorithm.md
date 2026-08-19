# Kadane's Algorithm

## Concept

Kadane's Algorithm is a dynamic programming technique used to find the maximum sum of a contiguous subarray.

The main idea is to keep track of the maximum sum of a subarray ending at the current position.

At every element, we decide whether to:

- Start a new subarray from the current element.
- Extend the existing subarray by including the current element.

## When to Use

Kadane's Algorithm is useful when:

- We need the maximum sum of a contiguous subarray.
- The problem asks for the best continuous segment.
- The array can contain positive and negative numbers.
- A brute-force solution would examine many subarrays.

## How It Works

For every element, maintain:

```text
currentSum
which represents the maximum sum of a subarray ending at the current element.

The decision is:

currentSum = max(arr[i], currentSum + arr[i])

Then maintain:

maxSum

which stores the best sum found so far.

maxSum = max(maxSum, currentSum)
Example

Given:

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

The maximum-sum contiguous subarray is:

[4, -1, 2, 1]

Its sum is:

4 - 1 + 2 + 1 = 6

Therefore:

Maximum Subarray Sum = 6
Algorithm
Set currentSum to the first element.
Set maxSum to the first element.
Traverse the remaining elements.
For each element:
Decide whether to start a new subarray.
Or extend the current subarray.
Update maxSum.
Return maxSum.
Java Example
int currentSum = arr[0];
int maxSum = arr[0];


for (int i = 1; i < arr.length; i++) {


    currentSum = Math.max(arr[i], currentSum + arr[i]);


    maxSum = Math.max(maxSum, currentSum);
}


System.out.println(maxSum);
Example Walkthrough

For:

arr = [-2, 1, -3, 4, -1, 2, 1]

At 4:

currentSum = max(4, -4 + 4)
           = 4

The previous negative sum is discarded.

Then:

4 + (-1) = 3
3 + 2 = 5
5 + 1 = 6

The maximum is:

6
Handling All Negative Numbers

Kadane's Algorithm must correctly handle arrays where every element is negative.

For example:

arr = [-5, -2, -8]

The answer is:

-2

Therefore, initializing both values to 0 can produce an incorrect answer.

A safer approach is:

int currentSum = arr[0];
int maxSum = arr[0];
Time Complexity

Kadane's Algorithm takes:

O(n)

time.

Each element is processed exactly once.

Space Complexity

Only a few variables are required:

O(1)

extra space.

Common Mistakes
Initializing the maximum sum to zero when all values may be negative.
Confusing maximum subarray with maximum subsequence.
Forgetting that the subarray must be contiguous.
Using nested loops when Kadane's Algorithm can solve the problem in linear time.
Variations

Kadane's Algorithm can be extended to:

Find the maximum subarray sum.
Find the actual maximum-sum subarray.
Find the minimum subarray sum.
Find maximum circular subarray sum.
Track the starting and ending indices of the best subarray.
Related Patterns
Dynamic Programming
Prefix Sum
Sliding Window
Greedy Technique
Related Problems
Maximum Subarray
Maximum Circular Subarray
Best Time to Buy and Sell Stock
Maximum Product Subarray
Maximum Sum Subarray