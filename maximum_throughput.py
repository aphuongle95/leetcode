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

def check_scalable(throughput: List[int], scaling_cost: List[int], budget: int, min_throughput: int, n: int):
    # check if we could scale other services so that it's throughputs are at least the min_throughput
    # only need to find the minimum scale for each service so that it's throughput exceed the minimum ones
    scales = []
    for t in throughput:
        scales.append(math.ceil(min_throughput / t) - 1)
    
    if np.dot(scales, scaling_cost) <= budget:
        return True
    return False

def getMaximumThroughput(throughput: List[int], scaling_cost: List[int], budget: int):
    n = len(throughput) # number of services
    max_throughput = 0
    indexes_decreasing = np.argsort(throughput)[::-1]
    throughput = [throughput[i] for i in indexes_decreasing]
    scaling_cost = [scaling_cost[i] for i in indexes_decreasing]
    
    # assume service at index i is the ones which give the min throughput, 
    # check what's the max scale can be
    for i in range(n):
        max_scale_i = math.floor(budget/scaling_cost[i])
        throughput_others = throughput.copy()
        throughput_others.pop(i)
        scaling_cost_others = scaling_cost.copy()
        scaling_cost_others.pop(i)
        can_scale = False
        can_skip = True
        for scale_i in reversed(range(max_scale_i+1)):
            curr_throughput = throughput[i] * (scale_i + 1) 
            if curr_throughput <= max_throughput: 
                can_skip = True
                break # it makes no sense to continue searching
            
            budget_left = budget - scale_i*scaling_cost[i]
            min_throughput = (scale_i+1)*throughput[i]
            
            can_scale = check_scalable(throughput_others, scaling_cost_others, budget_left, min_throughput, n)
            if can_scale:
                max_throughput = curr_throughput
        if can_skip:
            continue
    return max_throughput

class Test(unittest.TestCase):
    def test_get_maximum_throughput(self):
        self.assertEqual(getMaximumThroughput(throughput=[3,2,5],scaling_cost=[2,5,10],budget=28), 6)
        self.assertEqual(getMaximumThroughput(throughput=[7,3,4,6],scaling_cost=[2,5,4,3],budget=25), 9)
        self.assertEqual(getMaximumThroughput(throughput=[4,2,7],scaling_cost=[3,5,6],budget=32), 10) 
        self.assertEqual(getMaximumThroughput(throughput=[6,42,17,11,47,20,34],scaling_cost=[6,43,39,47,27,58,31],budget=289), 34) 
        
if __name__ == '__main__':
    unittest.main()
