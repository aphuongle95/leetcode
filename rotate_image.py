"""
https://leetcode.com/problems/rotate-image/
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000"""

import math
from typing import List
import unittest


class Solution:
    def rotate(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Observation:
        value at [i, j] will be at [j, n-1-i] after rotation
        when n is odd, value at the center [(n-1)/2, (n-1)/2] will stay the same
        """
        n = len(matrix)
        for i in range(math.floor((n-1)/2)+1):
            for j in range(math.floor(n/2)):
                t = [[i,j], [j, n-1-i], [n-1-i, n-1-j], [n-1-j, i]] # all affected indexes

                # replace = matrix[t[0][0]][t[0][1]] # use the first element to replace the second ones
                # keep = matrix[t[1][0]][t[1][1]] # keep the second element
                replace = matrix[t[0][0]][t[0][1]] # use this to replace the next element
                keep = 0
                for k in range(0, len(t)): 
                    keep = matrix[t[(k+1)%4][0]][t[(k+1)%4][1]] # keep the next element first
                    matrix[t[(k+1)%4][0]][t[(k+1)%4][1]] = replace
                    replace = keep
        return matrix
    
class Test(unittest.TestCase):
    def test_roate(self):
        self.assertEqual(Solution().rotate([[1,2,3],[4,5,6],[7,8,9]]), [[7,4,1],[8,5,2],[9,6,3]])
        self.assertEqual(Solution().rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]), [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])
        
if __name__ == "__main__":
    unittest.main()