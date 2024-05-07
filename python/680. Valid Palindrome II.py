"""
Given a string s, return true if the s can be palindrome
after deleting at most one character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false

Constraints:

1 <= s.length <= 10^5
s consists of lowercase English letters.
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        i = 0
        while i <= len(s)/2 and s[i] == s[-(i+1)]:
            i += 1
        s = s[i:len(s)-i] # O(n)
        return s[1:] == s[1:][::-1] or s[:-1] == s[:-1][::-1]

















































