"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
"""
from collections import deque


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        list_s = deque(s)
        zig_dict = {idx: '' for idx in range(numRows)}

        asc = 0
        desc = 0

        while list_s:
            if asc < numRows:
                string = list_s.popleft()
                zig_dict[asc] = zig_dict[asc] + string
                asc += 1
                if asc == numRows:
                    desc = numRows - 1
            else:
                string = list_s.popleft()
                desc -= 1
                zig_dict[desc] = zig_dict[desc] + string
                if desc == 0:
                    asc = 1

        result = ''.join([chrs for chrs in zig_dict.values()])

        return result
