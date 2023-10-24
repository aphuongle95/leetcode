"""
https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
import collections
from typing import List, Optional
import unittest

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # keep all values at each level in a queue
        # pop the queue to find elements at next level
        if root == None or root == []:
            return []
        
        q = collections.deque()
        q.append(root)
        l = [] # the whole list
        
        while q:
            li = []
            for i in range(len(q)): # loop through all nodes at this level
                t = q.popleft()
                li.append(t.val) # append to current list
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            l.append(li) # update whole list
                
        return l
                
                
        