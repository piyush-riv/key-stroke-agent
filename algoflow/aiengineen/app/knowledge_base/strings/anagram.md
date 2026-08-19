# Anagram

## Concept

An anagram is formed when two strings contain the same characters with the same frequencies, but possibly in a different order.

Examples:

```text
listen → silent
anagram → nagaram
evil → vile
Java Example
public static boolean isAnagram(String s, String t) {


    if (s.length() != t.length()) {
        return false;
    }


    int[] freq = new int[26];


    for (char c : s.toCharArray()) {
        freq[c - 'a']++;
    }


    for (char c : t.toCharArray()) {
        freq[c - 'a']--;
    }


    for (int x : freq) {
        if (x != 0) {
            return false;
        }
    }


    return true;
}
Sorting Approach

Another method is to convert both strings into character arrays and sort them.

Example:

listen → eilnst
silent → eilnst

Since the sorted representations are equal, the strings are anagrams.

Java Sorting Example
import java.util.Arrays;


public static boolean isAnagram(String s, String t) {


    if (s.length() != t.length()) {
        return false;
    }


    char[] a = s.toCharArray();
    char[] b = t.toCharArray();


    Arrays.sort(a);
    Arrays.sort(b);


    return Arrays.equals(a, b);
}
Frequency Array vs Sorting

Frequency array:

Time: O(n)
Space: O(1)

for a fixed alphabet.

Sorting:

Time: O(n log n)
Space: depends on implementation

The frequency approach is usually faster when the character set is small and known.

HashMap Approach

If the input can contain arbitrary characters, a HashMap can store character frequencies.

import java.util.HashMap;


HashMap<Character, Integer> map = new HashMap<>();


for (char c : s.toCharArray()) {
    map.put(c, map.getOrDefault(c, 0) + 1);
}

Then decrement the frequencies using the second string.

Time Complexity

Frequency array approach:

O(n)

Sorting approach:

O(n log n)

HashMap approach:

O(n)

on average.

Space Complexity

For a fixed alphabet:

O(1)

For a HashMap containing k distinct characters:

O(k)
Common Mistakes
Forgetting to check string lengths.
Comparing only whether characters exist instead of comparing frequencies.
Using a frequency array of size 26 when uppercase, Unicode, or arbitrary characters are allowed.
Forgetting to decrement frequencies for the second string.
Sorting unnecessarily when a frequency array can solve the problem in O(n).
Related Patterns
Frequency Array
HashMap
Sorting
Sliding Window
Character Counting
Related Problems
Valid Anagram
Group Anagrams
Find All Anagrams in a String
Permutation in String
Minimum Number of Steps to Make Two Strings Anagram