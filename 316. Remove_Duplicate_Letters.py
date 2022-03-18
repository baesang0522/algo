"""
Given a string s, remove duplicate letters so that every letter appears once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.


Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"


Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.


Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
"""
from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, stack = Counter(s), []

        for char in s:
            counter[char] -= 1
            if char in stack:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(char)

        return ''.join(stack)



# class Solution1:
#     def removeDuplicateLetters(self, s: str) -> str:
#         s_idx = {}
#         idx_s = {}
#         for idx, string in enumerate(list(s)):
#             s_idx.setdefault(string, []).append(idx)
#             idx_s.setdefault(idx, []).append(string)
#
#         comb_list = [sorted(list(cand)) for cand in product(*list(s_idx.values()))]
#
#         result_list = []
#         for l in comb_list:
#             convert_to_string = []
#             for idx in l:
#                 if idx in idx_s:
#                     convert_to_string.extend(idx_s[idx])
#             result_list.append(''.join(convert_to_string))
#         return min(result_list)
#
# "abdc" > "abcd"
# "acbd" > "acdb"





































