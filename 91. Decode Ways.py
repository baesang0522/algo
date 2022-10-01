"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.



Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
"""
s = "1201234"


class Solution(object):
    def numDecodings(self, s):
        if s[0] == "0":
            return 0
        s_list = list(s)

        dp = [0] * (len(s_list) + 1)
        dp[0], dp[1] = 1, 1

        for idx in range(2, len(s_list) + 1):
            cand = "".join(s_list[idx - 2:idx])
            if 1 <= int(cand[-1]) <= 9:
                dp[idx] += dp[idx - 1]
            if 10 <= int(cand) <= 26:
                dp[idx] += dp[idx - 2]

        return dp[-1]

cc = solution(s)





# dfs. 시간 초과(s="111111111111111111111111111111111111111111111")
# def sec_split_cand(last_list, c_list):
#     if "".join(last_list[:2]) in c_list:
#         return True
#     return False
#
#
# def is_available(after):
#     if after[0] != "0":
#         return True
#     return False
#
#
# class Solution(object):
#     def numDecodings(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if s[0] == "0":
#             return 0
#         result_list = []
#         s_list = list(s)
#         c_list = [str(idx) for idx in range(1, 27)]
#         if len(s) >= 2:
#             need_iter = [[[s_list[0]], s_list[1:]], [s_list[:2], s_list[2:]]]
#             if not sec_split_cand(s_list[:2], c_list):
#                 need_iter = need_iter[:1]
#         else:
#             need_iter = [[[s_list[0]], s_list[1:]]]
#
#         while need_iter:
#             cur_list, last_list = need_iter.pop()
#             if len(last_list) == 0:
#                 result_list.append(cur_list)
#                 continue
#             if is_available(last_list):
#                 new_cur_list = cur_list + [[last_list[0]]]
#                 new_last_list = last_list[1:]
#                 need_iter.append([new_cur_list, new_last_list])
#                 if len(last_list) >= 2 and sec_split_cand(last_list, c_list):
#                     new_cur_list = cur_list + [last_list[:2]]
#                     new_last_list = last_list[2:]
#                     need_iter.append([new_cur_list, new_last_list])
#
#         return len(result_list)






























