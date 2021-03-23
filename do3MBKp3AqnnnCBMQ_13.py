"""


Create a function that produces a random number that contains all numbers from
one to five, without any duplicates.

### Examples

    12345
    
    21345
    
    51234

### Notes

N/A

"""

import random
import itertools
from itertools import permutations
​
def numbers():
  
  Failsafe = 0
  
  while (Failsafe == 0):
    Chosen = random.randint(12345, 54321)
    Text = str(Chosen)
    
    Test_A = Text.count("1")
    Test_B = Text.count("2")
    Test_C = Text.count("3")
    Test_D = Text.count("4")
    Test_E = Text.count("5")
    
    if (Test_A == 1) and (Test_B == 1) and (Test_C == 1) and (Test_D == 1) and (Test_E == 1):
      Failsafe += 1
      return Chosen
    else:
      Failsafe = 0

