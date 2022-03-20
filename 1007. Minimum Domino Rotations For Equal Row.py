"""
In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino.
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same,
or all the values in bottoms are the same.

If it cannot be done, return -1.



Example 1:
Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
Output: 2

Explanation:
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2,
as indicated by the second figure.

Example 2:
Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
Output: -1

Explanation:
In this case, it is not possible to rotate the dominoes to make one row of values equal.
"""
from collections import defaultdict


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        len_a = len(tops)
        idx_dict = defaultdict(set)
        tops_idx_dict = defaultdict(set)
        bots_idx_dict = defaultdict(set)
        for idx, val in enumerate(zip(tops, bottoms)):
            idx_dict[val[0]].add(idx)
            idx_dict[val[1]].add(idx)
            tops_idx_dict[val[0]].add(idx)
            bots_idx_dict[val[1]].add(idx)

        result = -1
        for key, val in idx_dict.items():
            if len(val) == len_a:
                if len(bots_idx_dict[key]) >= len(tops_idx_dict[key]):
                    tmp = len(tops_idx_dict[key] - bots_idx_dict[key])
                elif len(tops_idx_dict[key]) >= len(bots_idx_dict[key]):
                    tmp = len(bots_idx_dict[key] - tops_idx_dict[key])
                else:
                    tmp = len(tops_idx_dict[key])

                if result == -1:
                    result = tmp
                else:
                    result = min(result, tmp)

        return result

