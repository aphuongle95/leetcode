"""
https://leetcode.com/problems/top-k-frequent-elements/
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size."""

from typing import List
from heapq import heappush, heappop
import unittest

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Approach 1: using heap
        count the frequencies of the elements in the list
        and then use heap to get the maximum frequencies
        Approach 2: using bucket sort
        convert the count dictionary to bucket list,
        where index of the bucket is the frequency
        """
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        
        # approach 1
        # h = []
        # for (n, f) in count.items():
        #     heappush(h, (-f, n)) # as it's meanheap, minus the frequency to get the maximum
        
        # l = []
        # for i in range(k):
        #     l.append(heappop(h)[1]) 
        
        # approach 2
        l = []
        # build bucket
        b = [[] for i in range(len(nums))]
        for (n, f) in count.items():
            b[f-1].append(n) # 1 <= f <= len(nums)
        print(b)
            
        for f in reversed(range(len(count))):
            for n in b[f]:
                l.append(n)
                if len(l) == k:
                    return l

class Test(unittest.TestCase):
    def test_top_k_frequent(self):
        self.assertEqual(Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 2), [1,2])
        self.assertEqual(Solution().topKFrequent(nums = [1], k = 1), [1])
        
if __name__ == "__main__":
    unittest.main()