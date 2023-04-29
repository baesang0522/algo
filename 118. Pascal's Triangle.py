"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]


Constraints:
1 <= numRows <= 30
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        dp = [[1], [1, 1]]
        for idx in range(2, numRows):
            be_idx_val = dp[idx - 1]
            cur_idx_val = []
            for jdx in range(len(be_idx_val) + 1):
                if jdx == 0 or jdx == len(be_idx_val):
                    cur_idx_val.append(1)
                    continue
                cur_idx_val.append(be_idx_val[jdx] + be_idx_val[jdx - 1])
            dp.append(cur_idx_val)
        return dp



