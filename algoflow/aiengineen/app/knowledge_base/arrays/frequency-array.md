# Frequency Array

## Concept

A frequency array is a data structure used to count how many times each value occurs.

Instead of repeatedly searching through an array to count occurrences, we maintain a separate array where each index represents a value and the stored number represents its frequency.

Frequency arrays are especially useful when the values belong to a small, known range.

## When to Use

Frequency arrays are useful when:

- We need to count occurrences of values.
- The input values have a small known range.
- We need to check whether two collections contain the same frequencies.
- We need to find duplicates.
- We need to find missing values.
- We need to perform frequency-based comparisons.
- The values are characters such as lowercase English letters.

## How It Works

Suppose:

```text
arr = [1, 2, 1, 3, 2, 1]
Create a frequency array.

For every value:

frequency[value]++

The resulting frequencies are:

Value:       0  1  2  3
Frequency:   0  3  2  1

Therefore:

1 occurs 3 times
2 occurs 2 times
3 occurs 1 time
Example

Given:

arr = [2, 3, 2, 1, 3, 2]

Create:

int[] freq = new int[4];

Process each value:

freq[2]++;
freq[3]++;
freq[2]++;
freq[1]++;
freq[3]++;
freq[2]++;

Final result:

freq[1] = 1
freq[2] = 3
freq[3] = 2
Algorithm
Determine the range of possible values.
Create a frequency array large enough for that range.
Traverse the input.
For every value x, increment frequency[x].
Use the frequency array to answer counting queries.
Java Example
int[] arr = {2, 3, 2, 1, 3, 2};


int[] freq = new int[4];


for (int x : arr) {
    freq[x]++;
}


for (int i = 0; i < freq.length; i++) {
    if (freq[i] > 0) {
        System.out.println(i + " -> " + freq[i]);
    }
}

Output:

1 -> 1
2 -> 3
3 -> 2
Frequency Array for Characters

Frequency arrays are commonly used with lowercase English letters.

There are 26 lowercase letters:

a -> 0
b -> 1
c -> 2
...
z -> 25

The frequency of a character can be stored using:

int[] freq = new int[26];


for (char c : str.toCharArray()) {
    freq[c - 'a']++;
}

For example:

str = "banana"

The frequencies are:

a -> 3
b -> 1
n -> 2
Comparing Two Strings

A frequency array can determine whether two strings are anagrams.

For:

str1 = "listen"
str2 = "silent"

Count the characters of the first string and subtract the characters of the second string.

If every frequency becomes zero, the strings contain exactly the same characters.

Java Anagram Example
int[] freq = new int[26];


for (char c : str1.toCharArray()) {
    freq[c - 'a']++;
}


for (char c : str2.toCharArray()) {
    freq[c - 'a']--;
}


boolean anagram = true;


for (int x : freq) {
    if (x != 0) {
        anagram = false;
        break;
    }
}


System.out.println(anagram);
Frequency Array vs HashMap

A frequency array is usually better when the value range is small and known.

Example:

lowercase English letters -> int[26]
digits -> int[10]

A HashMap is more appropriate when:

Values are very large.
Values are negative or arbitrary.
The range of possible values is unknown.
The input contains objects or strings as keys.
Time Complexity

Building the frequency array takes:

O(n)

Checking all frequencies takes:

O(k)

where k is the size of the possible value range.

For a fixed range such as 26 letters, this is effectively:

O(n)
Space Complexity

The frequency array uses:

O(k)

space.

For lowercase English letters:

O(26) = O(1)
Common Mistakes
Creating an array that is too small for the input values.
Forgetting that array indices must be valid.
Using freq[value] when values can be negative.
Using a frequency array when the value range is extremely large.
Forgetting to reset the frequency array between independent test cases.
Assuming a character string only contains lowercase letters.
Related Patterns
HashMap
Counting
Prefix Frequency
Sliding Window
Two Pointers
Sorting
Related Problems
Valid Anagram
First Unique Character in a String
Find the Duplicate Number
Majority Element
Counting Frequencies
Character Frequency
Group Anagrams