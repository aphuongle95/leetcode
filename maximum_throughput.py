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

def getMaximumThroughput(throughput: List[int], scaling_cost: List[int], budget: int):
    n = len(throughput) # number of services
    # sort the arrays so that the service with smaller throughput comes first
    indexes = np.argsort(throughput)
    throughput = np.array(throughput)[indexes]
    scaling_cost = np.array(scaling_cost)[indexes]
    
    max_scale_for_biggest_service = math.floor(budget/scaling_cost[0])
    throughput_others = throughput[1:]
    scaling_cost_others = scaling_cost[1:]
    can_scale = False
    for scale_for_biggest_service in reversed(range(max_scale_for_biggest_service+1)):
        budget_left = budget - scale_for_biggest_service*scaling_cost[0]
        min_throughput = (scale_for_biggest_service+1)*throughput[0]
        can_scale = check_scalable(throughput_others, scaling_cost_others, budget_left, min_throughput, n)
        if can_scale:
            return throughput[0] * (scale_for_biggest_service + 1)    
            

class Test(unittest.TestCase):
    def test_get_maximum_throughput(self):
        self.assertEqual(getMaximumThroughput(throughput=[3,2,5],scaling_cost=[2,5,10],budget=28), 6)
        self.assertEqual(getMaximumThroughput(throughput=[7,3,4,6],scaling_cost=[2,5,4,3],budget=25), 9)
        self.assertEqual(getMaximumThroughput(throughput=[4,2,7],scaling_cost=[3,5,6],budget=32), 10) 
        
if __name__ == '__main__':
    unittest.main()
