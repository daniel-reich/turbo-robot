"""


Create a function that returns the minimum number of **swaps** it takes to
transform a **binary string** into a string of **alternating 0s and 1s**. A
swap is switching from a 0 to a 1 or vice versa.

### Examples

    min_swaps("010010111") ➞ 4
    
    # Two possible conversions:
    #   1. "101010101" (4 swaps)
    #   2. "010101010" (5 swaps)
    
    min_swaps("10101010") ➞ 0
    
    min_swaps("10010") ➞ 2

### Notes

N/A

"""

def min_swaps(string):
  alternative1 = "01" * len(string);
  alternative2 = "10" * len(string);
  return min(positional_differences(alternative1,string) , positional_differences(alternative2,string) );
  
def positional_differences(string,other):
  return sum([a!=b for a,b in zip(string , other)]);

