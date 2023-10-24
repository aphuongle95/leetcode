"""
https://leetcode.com/problems/number-of-islands/
Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

import collections
from typing import List
import unittest


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set() # all the visited elements 
        num_rows = len(grid)
        num_cols = len(grid[0])
        num_islands = 0
        
        def bfs(rt: int, ct: int):
            """search for the whole island

            Args:
                rt (int): row of first found element of the island
                ct (int): col of first found element of the island
            """
            q = collections.deque() # a queue of all the element to search
            q.append((rt, ct))
            visited.add((rt, ct))
            
            while q: # if the island is still extendable
                ri, ci = q.popleft()
                directions = [[0,1], [1,0], [0,-1], [-1,0]]
                for dr, dc in directions:
                    r, c = ri + dr, ci + dc
                    if r in range(num_rows) and c in range(num_cols): # check if in range
                        if (r,c) not in visited: # check if visited
                            visited.add((r,c))
                            if grid[r][c] == "1":
                                q.append((r, c))
                            
            
        for r in range(num_rows):
            for c in range(num_cols):
                if (r,c) not in visited and grid[r][c] == "1": # new island
                    bfs(r, c) # extend the island
                    num_islands += 1
        return num_islands

class Test(unittest.TestCase):
    def test_num_islands(self):
        self.assertEqual(Solution().numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]), 1)
        self.assertEqual(Solution().numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]), 3)
        
if __name__ == "__main__":
    unittest.main()