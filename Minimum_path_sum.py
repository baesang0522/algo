"""
https://leetcode.com/problems/minimum-path-sum/
"""


class Solution:
    def minPathSum(self, grid) -> int:
        len_row, len_col = len(grid), len(grid[0])
        d_grid = [[0 for _ in range(len_col)] for _ in range(len_row)]
        d_grid[0][0] = grid[0][0]

        for idx in range(len(d_grid)):
            for jdx in range(len(d_grid[idx])):
                if idx == 0 and jdx == 0:
                    continue
                elif idx > 0 and jdx > 0:
                    d_grid[idx][jdx] = min(d_grid[idx - 1][jdx], d_grid[idx][jdx-1]) + grid[idx][jdx]
                elif idx > 0 and jdx == 0:
                    d_grid[idx][jdx] = grid[idx][jdx] + d_grid[idx - 1][jdx]
                elif jdx > 0 and idx == 0:
                    d_grid[idx][jdx] = grid[idx][jdx] + d_grid[idx][jdx - 1]

        return d_grid[-1][-1]