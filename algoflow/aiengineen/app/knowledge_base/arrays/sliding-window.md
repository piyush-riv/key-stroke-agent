\# Sliding Window Technique



\## Concept



The sliding window technique is used to solve problems involving a continuous or contiguous portion of an array or string.



A window represents a range of elements between two boundaries, usually called `left` and `right`.



Instead of repeatedly calculating the result for every possible subarray or substring, the window is expanded or contracted as we move through the data.



This can reduce many brute-force O(n²) solutions to O(n).



\## When to Use



Sliding window is commonly useful when:



\- The problem asks about a contiguous subarray.

\- The problem asks about a substring.

\- We need the longest or shortest subarray satisfying a condition.

\- We need the maximum or minimum sum of a fixed-size subarray.

\- We need to maintain information about the current range.

\- A brute-force solution checks many overlapping ranges.



\## Types of Sliding Window



There are two major types:



\### Fixed-Size Window



The window always has the same size.



Example:



Find the maximum sum of any subarray of size `k`.



If:



```text

arr = \[2, 1, 5, 1, 3, 2]

k = 3

The windows are:



\[2, 1, 5]

\[1, 5, 1]

\[5, 1, 3]

\[1, 3, 2]



Instead of calculating every sum from scratch, remove the element leaving the window and add the new element entering it.



Variable-Size Window



The window size changes depending on a condition.



Example:



Find the longest substring without repeating characters.



The right pointer expands the window.



If the window becomes invalid, move the left pointer until the window becomes valid again.



How It Works



A typical sliding window has two pointers:



left

right



Initially:



left = 0

right = 0



Move right to expand the window.



When the window violates the required condition, move left to shrink the window.



The general pattern is:



Expand → Check condition → Shrink if necessary → Update answer

Example



Find the maximum sum of a subarray of size 3.



Given:



arr = \[2, 1, 5, 1, 3, 2]

k = 3



First window:



2 + 1 + 5 = 8



Move the window one position:



Remove 2 and add 1:



8 - 2 + 1 = 7



Next:



7 - 1 + 3 = 9



Next:



9 - 5 + 2 = 6



Maximum sum:



9

Algorithm



For a fixed-size window:



Calculate the sum of the first k elements.

Store it as the current maximum.

Move the window one position at a time.

Remove the element leaving the window.

Add the element entering the window.

Update the maximum.

Continue until the end of the array.

Java Example

int k = 3;

int sum = 0;





for (int i = 0; i < k; i++) {

&#x20;   sum += arr\[i];

}





int max = sum;





for (int i = k; i < arr.length; i++) {

&#x20;   sum += arr\[i];

&#x20;   sum -= arr\[i - k];





&#x20;   max = Math.max(max, sum);

}





System.out.println(max);

Variable-Size Window Pattern



A common variable-size pattern is:



int left = 0;





for (int right = 0; right < arr.length; right++) {





&#x20;   // Add arr\[right] to the current window





&#x20;   while (/\* window is invalid \*/) {





&#x20;       // Remove arr\[left] from the window

&#x20;       left++;

&#x20;   }





&#x20;   // Update the answer

}



The exact condition depends on the problem.



Time Complexity



Most sliding window solutions run in:



O(n)



Although there may be a nested while loop, the left and right pointers generally move forward only, so each element is processed a limited number of times.



Space Complexity



Basic sliding window solutions often use:



O(1)



extra space.



However, if we maintain a frequency map or set, the space complexity may become:



O(k)



or:



O(n)



depending on the problem.



Common Mistakes

Confusing a subarray with a subsequence.

Using sliding window when the problem does not involve a contiguous range.

Forgetting to remove the element leaving the window.

Updating the answer before the window satisfies the required condition.

Using a fixed-size window when the problem requires a variable-size window.

Assuming every sliding window problem can be solved without a HashMap or Set.

Sliding Window vs Two Pointers



Sliding window is closely related to two pointers.



Two pointers are a broader technique where two indices move through a data structure.



Sliding window specifically maintains a continuous range between two pointers.



Therefore:



Two Pointers

&#x20;    ↓

Can represent a range

&#x20;    ↓

Sliding Window

Related Patterns

Two Pointer Technique

Prefix Sum

Hashing

Frequency Counting

Fast and Slow Pointers

Related Problems

Maximum Sum Subarray of Size K

Longest Substring Without Repeating Characters

Minimum Size Subarray Sum

Longest Repeating Character Replacement

Permutation in String

Minimum Window Substring

Maximum Number of Vowels in a Substring of Given Length

