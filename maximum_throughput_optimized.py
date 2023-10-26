#!/bin/python3

import collections
import math
import os
import random
import re
import sys
from typing import List, Tuple
import unittest

import numpy as np
#
# Complete the 'getMaximumThroughput' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY throughput
#  2. INTEGER_ARRAY scaling_cost
#  3. INTEGER budget
#

max_scales = []

def check_scalable(throughput: List[int], scaling_cost: List[int], budget: int, min_throughput: int, n: int):
    # check if we could scale other services so that it's throughputs are at least the min_throughput
    # only need to find the minimum scale for each service so that it's throughput exceed the minimum ones
    scales = []
    for t in throughput:
        scales.append(math.ceil(min_throughput / t) - 1)
    
    if np.dot(scales, scaling_cost) <= budget:
        global max_scales
        max_scales = scales
        return True
    return False

def getMaximumThroughput(throughput: List[int], scaling_cost: List[int], budget: int):
    """Solution:
    Assume a number to be the maximum throughput,
    use binary search on a range to find a better throughput
    """
    low = min(throughput)
    high = math.ceil(budget) / min(scaling_cost) * max(throughput)
    while low < high:
        mid = math.floor(low + high) / 2
        if check_scalable(throughput, scaling_cost, budget, mid):
            low = mid
        else:
            high = mid
            
    return min(np.dot(max_scales, throughput))

"""Improving solution:
using binary search
the minimum throughput
"""
 
class Test(unittest.TestCase):
    def test_get_maximum_throughput(self):
        self.assertEqual(getMaximumThroughput(throughput=[3,2,5],scaling_cost=[2,5,10],budget=28), 6)
        self.assertEqual(getMaximumThroughput(throughput=[7,3,4,6],scaling_cost=[2,5,4,3],budget=25), 9)
        self.assertEqual(getMaximumThroughput(throughput=[4,2,7],scaling_cost=[3,5,6],budget=32), 10) 
        self.assertEqual(getMaximumThroughput(throughput=[6,42,17,11,47,20,34],scaling_cost=[6,43,39,47,27,58,31],budget=289), 34) 
        
if __name__ == '__main__':
    unittest.main()
    # print(knapSack(W, wt, val, n))
