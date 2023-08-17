# Scheduling is how the processor decides which jobs (processes) get to use the processor and for how long. This can cause a lot of problems. For example, a long-running process might use the entire CPU and block all the other processes from executing. One solution is Shortest Job First (SJF), which you will implement in this challenge.

# SJF works by letting the shortest jobs take the CPU first. If the jobs are the same size then break the tie with First In First Out (FIFO). The idea is that the shorter jobs will finish quicker, so theoretically jobs won't get frozen because of large jobs. (In practice they're frozen because of small jobs).