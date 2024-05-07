"""
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.



Example 1:
Input: low = 100, high = 300
Output: [123,234]

Example 2:
Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]


Constraints:

10 <= low <= high <= 10^9
"""
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        str_int = ''.join(str(num) for num in range(1, 10))
        low_len, high_len, idx = len(str(low)), len(str(high)), 0
        result_list = []

        while True:
            num = int(str_int[idx:idx+low_len])
            if num == 123456789 and low <= num <= high:
                result_list.append(123456789)
                break
            elif num > high or num == 123456789:
                break

            if (result_list and num < result_list[-1]) or (len(str(num)) < low_len):
                idx, low_len = 0, low_len + 1
                continue

            if num >= low:
                result_list.append(num)
            idx += 1
        return result_list

