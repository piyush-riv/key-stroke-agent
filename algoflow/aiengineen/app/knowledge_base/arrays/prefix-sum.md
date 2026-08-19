# Prefix Sum

## Concept

Prefix Sum is a technique used to quickly calculate the sum of elements in a subarray.

A prefix sum array stores the cumulative sum of elements from the beginning of the array up to each position.

Instead of repeatedly calculating the sum of a range, we preprocess the array once and then answer range-sum queries efficiently.

## When to Use

Prefix Sum is commonly useful when:

- We need the sum of a subarray.
- There are multiple range-sum queries.
- The array does not change during the queries.
- We need to find subarrays with a particular sum.
- We want to reduce repeated summation from O(n) to O(1).
- The problem involves cumulative values.

## How It Works

Given:

```text
arr = [2, 4, 1, 3, 5]
Create a prefix sum array:

prefix = [2, 6, 7, 10, 15]

Each value represents the sum from index 0 to that index.

For example:

prefix[2] = 2 + 4 + 1 = 7
Range Sum Formula

To calculate the sum from index left to index right:

sum(left, right) = prefix[right] - prefix[left - 1]

When left = 0:

sum(0, right) = prefix[right]

A convenient implementation uses a prefix array of size n + 1:

prefix[0] = 0
prefix[i + 1] = prefix[i] + arr[i]

Then:

sum(left, right) = prefix[right + 1] - prefix[left]
Example

Given:

arr = [2, 4, 1, 3, 5]

The prefix array is:

prefix = [0, 2, 6, 7, 10, 15]

Find the sum from index 1 to index 3.

The elements are:

[4, 1, 3]

Using the formula:

prefix[4] - prefix[1]
= 10 - 2
= 8

Therefore the range sum is:

8
Algorithm
Create a prefix array of size n + 1.
Set prefix[0] = 0.
For every element:
Add the current element to the previous prefix sum.
For a range [left, right]:
Calculate prefix[right + 1] - prefix[left].
Return the result.
Java Example
int[] prefix = new int[arr.length + 1];


for (int i = 0; i < arr.length; i++) {
    prefix[i + 1] = prefix[i] + arr[i];
}


int left = 1;
int right = 3;


int sum = prefix[right + 1] - prefix[left];


System.out.println(sum);
Prefix Sum for Subarray Sum

Prefix sums can also be combined with a HashMap to find subarrays having a particular sum.

Suppose the current prefix sum is:

currentSum

We need a previous prefix sum equal to:

currentSum - target

If such a prefix sum exists, the elements between those two positions have the required sum.

This technique is commonly used for the problem:

Subarray Sum Equals K
Time Complexity

Building the prefix sum array takes:

O(n)

Each range-sum query takes:

O(1)

Therefore, for q queries:

O(n + q)
Space Complexity

The prefix array requires:

O(n)

extra space.

Common Mistakes
Using the wrong indices in the range-sum formula.
Forgetting the extra zero at the beginning of the prefix array.
Confusing prefix sum with suffix sum.
Using prefix sum when the array changes frequently without considering an appropriate data structure.
Integer overflow when the array contains very large values.
Prefix Sum vs Sliding Window

Prefix Sum is useful when we need to answer range-sum queries efficiently.

Sliding Window is useful when maintaining a moving contiguous range.

Prefix Sum can often work with negative numbers.

Some sliding-window techniques, especially those based on expanding and shrinking according to a sum condition, may require additional assumptions such as non-negative values.

Related Patterns
Subarray Sum
HashMap
Sliding Window
Difference Array
Suffix Sum
Cumulative Sum
Related Problems
Range Sum Query
Subarray Sum Equals K
Continuous Subarray Sum
Find Pivot Index
Product of Array Except Self
Maximum Size Subarray Sum Equals K