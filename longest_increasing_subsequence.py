"""
Given an integer array nums, return the length of the longest strictly increasing 
subsequence.

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""

from ast import List
import unittest
import numpy as np

class Solution:
    def lengthOfLIS(self, nums: List(int)) -> int:
        """Approach 1:
        Make the array shorter by iterating through the array reversely.
        For each element, we find the longest subsequence from that element towards the end of the array by comparing the computed lenghts
        Approach 2: starred
        Keep an array of increasing elements, 
        and use a binary search to replace element when it's not increasing

        Args:
            nums (List[int]): _description_

        Returns:
            int: _description_
        """
        # Approach 1
        # n = len(nums)
        # lis = [1] * n # keeps len of longest subsequence from the element towards end of array
        # for i in reversed(range(len(nums))): # index
        #     for j in range(i+1, n): # finds next element to add up to the sequence
        #         if nums[j] > nums[i] and lis[j] + 1 > lis[i]: # assume we add up this number, what follows will be its longest subsequence
        #             lis[i] = 1 + lis[j]
        # return max(lis)      
        # Approach 2
        n = len(nums)
        ans = []
    
        ans.append(nums[0])
    
        for i in range(1, n):
            if nums[i] > ans[-1]:
                ans.append(nums[i])
            else:
                low = 0
                high = len(ans) - 1
                while low < high:
                    mid = low + (high - low) // 2
                    if ans[mid] < nums[i]:
                        low = mid + 1
                    else:
                        high = mid
                ans[low] = nums[i]

        return len(ans)
   
                
    
class Test(unittest.TestCase):
    def test_length_of_LIS(self):
        # self.assertEqual(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]), 4)
        # self.assertEqual(Solution().lengthOfLIS([0,1,0,3,2,3]), 4)
        # self.assertEqual(Solution().lengthOfLIS([7,7,7,7,7,7,7]), 1)
        self.assertEqual(Solution().lengthOfLIS([10,9,2,5,3,7,101,18,3,4,5,6,7]), 6)
        

if __name__ == "__main__":
    unittest.main()