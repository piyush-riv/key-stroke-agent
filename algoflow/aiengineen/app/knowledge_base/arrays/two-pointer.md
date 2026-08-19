\# Two Pointer Technique



\## Concept



The two pointer technique uses two indices to traverse an array, string, or other linear data structure.



The pointers can move toward each other, move in the same direction, or move at different speeds depending on the problem.



The main idea is to avoid unnecessary nested loops by intelligently moving one or both pointers.



\## When to Use



Two pointers are commonly useful when:



\- The array is sorted.

\- We need to find a pair of elements satisfying a condition.

\- We need to compare elements from opposite ends.

\- We need to remove duplicates.

\- We need to partition or rearrange an array.

\- We need to reduce an O(n²) pair-search into O(n).

\- We are working with strings or arrays where two positions can represent the current search range.



\## How It Works



A common approach is to place:



\- `left` at the beginning of the array.

\- `right` at the end of the array.



For a sorted array:



\- If the current sum is smaller than the target, move `left` forward.

\- If the current sum is larger than the target, move `right` backward.

\- If the sum equals the target, the required pair has been found.



The pointers eliminate portions of the search space that no longer need to be considered.



\## Example



Given:



```text

arr = \[1, 2, 3, 4, 6]

target = 6Start:



left = 0

right = 4



Check:



1 + 6 = 7



The sum is too large, so move right.



Now:



1 + 4 = 5



The sum is too small, so move left.



Now:



2 + 4 = 6



The target is found.



Algorithm

Set left = 0.

Set right = n - 1.

While left < right:

Calculate the required condition.

If the answer is found, return it.

If the value is too small, move left.

If the value is too large, move right.

Stop when the pointers meet.

Java Example

int left = 0;

int right = arr.length - 1;





while (left < right) {





&#x20;   int sum = arr\[left] + arr\[right];





&#x20;   if (sum == target) {

&#x20;       System.out.println("Pair found");

&#x20;       break;

&#x20;   }

&#x20;   else if (sum < target) {

&#x20;       left++;

&#x20;   }

&#x20;   else {

&#x20;       right--;

&#x20;   }

}

Time Complexity



Most standard two pointer solutions run in:



O(n)



Space Complexity



Most basic two pointer solutions use:



O(1)



extra space.



Common Mistakes

Do not automatically use two pointers on an unsorted array.

Make sure the pointer movement is correct.

Make sure the loop condition is correct.

Do not sort the array if the original order must be preserved.

Not every pair-search problem can be solved using two pointers.

Related Patterns

Sliding Window

Fast and Slow Pointers

Binary Search

Sorting

Related Problems

Two Sum II

Container With Most Water

3Sum

4Sum

Remove Duplicates from Sorted Array

Valid Palindrome

