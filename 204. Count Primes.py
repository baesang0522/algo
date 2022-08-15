"""
Given an integer n, return the number of prime numbers that are strictly less than n.


Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0

Constraints:

0 <= n <= 5 * 106
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True for i in range(n)]
        i = 2
        while (i * i < n):
            if (primes[i] == True):
                for p in range(i * i, n, i):
                    primes[p] = False
            i += 1

        counter = 0
        for i in range(2, len(primes)):
            if primes[i]:
                counter += 1
        return counter



