# Write a function that returns the minimum number of breaks needed to split a bar of "n x m" size, into "1 x 1" squares.

import math

def break_chocolate(n, m):
    if m==0 or n==0:
      return 0 # actually it should raise an error
    if n == 1:
      print(f"min break for {m}, {n} is {m-1}")
      return m - 1
    if m == 1:
      print(f"min break for {m}, {n} is {n-1}")
      return n - 1
     
    # break into m pieces using m-1 breaks and then for each piece, break n-1 times into unit squares
    min_breaks = min ( (m-1) + m * (n-1), (n-1) + n * (m-1)) 
    
    # break horizontally
    for i in range(1, math.floor(m/2)):
      # break in 2 pieces
      num_breaks = 1 + break_chocolate(i, n) + break_chocolate(m-i, n)
      if num_breaks < min_breaks:
        min_breaks = num_breaks
        
    # break vertically
#     for i in range(1, math.floor(n/2)):
#       # break in 2 pieces
#       num_breaks = 1 + break_chocolate(i, m) + break_chocolate(n-i, m)
#       if num_breaks < min_breaks:
#         min_breaks = num_breaks
    
    print(f"min break for {m}, {n} is {min_breaks}")
    return min_breaks