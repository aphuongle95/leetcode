"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Returns:
    _type_: _description_
"""

import unittest


class Solution(object):
    def twoSum(self, nums, target):
         
        keep = {} # keep number to find and index

        for i in range(len(nums)):
            n = nums[i]
            if n in keep:
                # return the first index and this
                return [keep[n], i] 

            find = target - n 
            keep[find] = i 
    
class Test(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(Solution().twoSum([2,7,11,15], 9), [0,1])
        self.assertEqual(Solution().twoSum([3,2,4], 6), [1,2])
        self.assertEqual(Solution().twoSum([3,3], 6), [0,1])
        
if __name__ == "__main__":
    unittest.main()