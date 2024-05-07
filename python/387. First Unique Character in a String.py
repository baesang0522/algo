"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1


Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""
from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        result_dict = defaultdict(list)

        for idx, c in enumerate(s):
            result_dict[c].append(idx)

        result = []
        for val in result_dict.values():
            if len(val) == 1:
                result.extend(val)
        return min(result) if result else -1























