"""
Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row. 

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
"""

from typing import List
import unittest


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        # sum the element backwards, keep the sum at the parent index itself
        for i in reversed(range(len(triangle) - 1)): # from second last row to 0
            for j in range(i+1): # from 0 to i
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        
        return triangle[0][0]
            
class Test(unittest.TestCase):
    def test_minimumTotal(self):
        self.assertEqual(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]), 11)
        self.assertEqual(Solution().minimumTotal([[-1],[2,3],[1,-1,-3]]), -1)


if __name__ == "__main__":
    unittest.main()
