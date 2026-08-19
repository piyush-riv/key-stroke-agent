# Palindrome

## Concept

A palindrome is a sequence that reads the same from left to right and right to left.

Examples:

```text
madam
racecar
level
121
Example Usage
String s = "racecar";


if (isPalindrome(s)) {
    System.out.println("Palindrome");
} else {
    System.out.println("Not Palindrome");
}

Output:

Palindrome
Palindrome Ignoring Case

Sometimes the problem considers uppercase and lowercase letters equivalent.

For example:

RaceCar

should be considered a palindrome.

We can convert the string to lowercase:

s = s.toLowerCase();

Then perform the normal two pointer comparison.

Palindrome Ignoring Spaces and Symbols

Some problems require ignoring spaces, punctuation, and capitalization.

For example:

"A man, a plan, a canal: Panama"

is considered a palindrome when only alphanumeric characters are considered.

A two pointer solution can skip characters that are not letters or digits.

Java Example
public static boolean isValidPalindrome(String s) {


    int left = 0;
    int right = s.length() - 1;


    while (left < right) {


        while (left < right &&
               !Character.isLetterOrDigit(s.charAt(left))) {
            left++;
        }


        while (left < right &&
               !Character.isLetterOrDigit(s.charAt(right))) {
            right--;
        }


        if (Character.toLowerCase(s.charAt(left)) !=
            Character.toLowerCase(s.charAt(right))) {
            return false;
        }


        left++;
        right--;
    }


    return true;
}
Number Palindrome

A number can also be checked for palindrome.

Example:

121

is a palindrome because:

121 -> 121

One approach is to reverse the number and compare it with the original.

Java Number Example
public static boolean isNumberPalindrome(int n) {


    if (n < 0) {
        return false;
    }


    int original = n;
    int reversed = 0;


    while (n > 0) {


        int digit = n % 10;


        reversed = reversed * 10 + digit;


        n /= 10;
    }


    return original == reversed;
}
Complexity

For a string of length n, the two pointer approach examines each character at most once.

Time complexity:

O(n)

Space complexity:

O(1)

when no additional string or array is created.

Common Mistakes
Comparing only the first and last characters.
Forgetting to move both pointers.
Using left <= right when left < right is sufficient.
Forgetting to handle uppercase and lowercase when required.
Forgetting to skip spaces and punctuation when required.
Creating unnecessary reversed strings when an O(1)-space solution is possible.
Palindrome and Two Pointers

Palindrome checking is one of the simplest applications of the two pointer technique.

The general pattern is:

left →       ← right


Compare both ends
Move inward
Repeat

This pattern is useful for many problems involving symmetry.

Related Patterns
Two Pointer Technique
String Traversal
Character Frequency
Recursion
Dynamic Programming
Related Problems
Valid Palindrome
Valid Palindrome II
Palindrome Linked List
Longest Palindromic Substring
Palindromic Substrings
Palindrome Number
Shortest Palindrome