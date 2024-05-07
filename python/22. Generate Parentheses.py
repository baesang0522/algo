"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        string, result_list = "", []
        def combination(left, right, string, result_list):
            if left == 0 and right == 0:
                result_list.append(string)

            if left > 0:
                combination(left-1, right, string + '(', result_list)
            if right > 0 and left < right:
                combination(left, right-1, string+')', result_list)

        combination(left=n, right=n, string=string, result_list=result_list)
        return list(set(result_list))

s = Solution()
aa = s.generateParenthesis(n=3)














