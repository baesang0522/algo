"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches
the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c]
represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east,
and west if the neighboring cell's height is less than or equal to the current cell's height.
Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from
cell (ri, ci) to both the Pacific and Atlantic oceans.

Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

Example 2:
Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
"""
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row_move = [1, -1, 0, 0]
        col_move = [0, 0, 1, -1]

        m, n = len(heights), len(heights[0])
        need_visit = []
        to_p = []
        to_a = []
        for x in range(len(heights)):
            for y in range(len(heights[0])):
                need_visit.append([x, y])
                visited = []
                while need_visit:
                    cur_xy = need_visit.pop()
                    visited.append(cur_xy)
                    if cur_xy[0] == 0 or cur_xy[1] == 0:
                        to_p.append([x, y])
                        need_visit = []
                        break
                    for mv_x, mv_y in zip(row_move, col_move):
                        mv_xy = [cur_xy[0] + mv_x, cur_xy[1] + mv_y]
                        if 0 <= mv_xy[0] <= m - 1 and 0 <= mv_xy[1] <= n - 1 and is_available(heights, cur_xy, mv_xy) \
                                and mv_xy not in visited:
                            need_visit.append(mv_xy)

        while to_p:
            start_xy = to_p.pop()
            need_visit.append(start_xy)
            visited = []
            while need_visit:
                cur_xy = need_visit.pop()
                visited.append(cur_xy)
                if cur_xy[0] == m - 1 or cur_xy[1] == n - 1:
                    to_a.append(start_xy)
                    need_visit = []
                    break
                for mv_x, mv_y in zip(row_move, col_move):
                    mv_xy = [cur_xy[0] + mv_x, cur_xy[1] + mv_y]
                    if 0 <= mv_xy[0] <= m - 1 and 0 <= mv_xy[1] <= n - 1 and is_available(heights, cur_xy, mv_xy) \
                            and mv_xy not in visited:
                        need_visit.append(mv_xy)
        return to_a


def is_available(h_list, cur_xy, mv_xy):
    if h_list[cur_xy[0]][cur_xy[-1]] >= h_list[mv_xy[0]][mv_xy[-1]]:
        return True
    return False







































