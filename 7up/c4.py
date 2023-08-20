# Scheduling is how the processor decides which jobs (processes) get to use the processor and for how long. This can cause a lot of problems. For example, a long-running process might use the entire CPU and block all the other processes from executing. One solution is Shortest Job First (SJF), which you will implement in this challenge.

# SJF works by letting the shortest jobs take the CPU first. If the jobs are the same size then break the tie with First In First Out (FIFO). The idea is that the shorter jobs will finish quicker, so theoretically jobs won't get frozen because of large jobs. (In practice they're frozen because of small jobs).

# You will be implementing:

#   def SJF(jobs, index)
# It takes in:

# "jobs" a non-empty array of positive integers. They represent the clock-cycles(cc) needed to finish the job.
# "index" a positive integer. That represents the job we're interested in.
# SJF returns:

# A positive integer representing the cc it takes to complete the job at index.
# Here's an example:

# SJF([3, 10, 20, 1, 2], 0)
# at 0cc [3, 10, 20, 1, 2] jobs[3] starts
# at 1cc [3, 10, 20, 0, 2] jobs[3] finishes, jobs[4] starts
# at 3cc [3, 10, 20, 0, 0] jobs[4] finishes, jobs[0] starts
# at 6cc [0, 10, 20, 0, 0] jobs[0] finishes

from typing import List
import unittest

class Solution:
    """The requirement only asks to return the time it takes to finish the job at index.
    An easy way to do it is find those jobs that are smaller than this job, 
    and simply sum up the times taken by smaller jobs and this ones.
    But it is like cheating, as it doesn't show how the shortest job first algorithm works.
    For this reason, I implement `getOrder` function to get the order of the jobs
    """
    def get_order(self, tasks: List[int]) -> List[int]:
        """Get order of the jobs processed

        Args:
            tasks (List[int]): list of time taken by job at index

        Returns:
            List[int]: order of the jobs to be processed by index
        """
        return sorted(range(len(tasks)), key=lambda k: tasks[k])
    
    def SJF(self, jobs: List[int], index: 0) -> int:
        """Get the time taken from beginning tills the job at index is finished

        Args:
            jobs (List[int]): list of time taken by jobs in the queue 
            index (0): the index of the job that needs to be processed

        Returns:
            int: the time taken till the job at index is finished
        """
        orders = self.get_order(jobs)
        time_taken = 0
        for ind in orders:
            time_taken += jobs[ind]
            if ind == index:
                break
        return time_taken
        

class Test(unittest.TestCase):
    def test_get_order(self):
        self.assertEqual(Solution().get_order([2, 3, 1, 4, 5, 3]), [2, 0, 1, 5, 3, 4])
        
    def test_SJF(self):
        self.assertEqual(Solution().SJF([3, 10, 20, 1, 2], 0), 6)

if __name__ == "__main__":
    unittest.main()