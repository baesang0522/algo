"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into
a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false


Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""
from typing import List
from copy import deepcopy


# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         def recursive(s, wordDict):
#             if not wordDict:
#                 return False
#             diff_s = deepcopy(s)
#             for word in wordDict:
#                 diff_s = diff_s.replace(word, " ").strip()
#                 if not diff_s:
#                     return True
#             if diff_s:
#                 wordDict = wordDict[1:]
#                 return recursive(s, wordDict)
#         return recursive(s, wordDict)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * (len(s))
        wordDict = set(wordDict)

        for i in range(1, len(s) + 1):
            for j in range(i):
                word = s[j:i]
                if dp[j] and word in wordDict:
                    if j + len(word) == len(s):
                        return True
                    dp[i] = True
                    break

        return dp[-1]




