"""


You are given a list of `0`s and `1`s, like the one below:

    [0, 1, 0, 0, 0, 1, 1, 1, 0, 1]
    
    # The first element, a 0, and the last element, a 1 are both unhappy.
    # The second element, a 1 is unhappy.
    # The second-to-last element, a 0 is unhappy.
    # All other numbers in this list are happy.

A `1` is **unhappy** if the digit to its left and the digit to its right are
both 0s. A `0` is **unhappy** if the digit to its left and the digit to its
right are both 1s. If a number has only one neighbor, it is **unhappy** if its
only neighbor is different. Otherwise, a number is **happy**.

Write a function that takes in a list of `0`s and `1`s and outputs the
**portion of numbers which are happy**. The total portion of numbers which are
happy can be represented as:

    portion of happy 0s = # happy 0s / total # 0s
    portion of happy 1s = # happy 1s / total # 1s
    portion of happy numbers = (portion of happy 0s + portion of happy 1s) / 2

In the example above, `0.6` is the number of happy numbers.

### Examples

    portion_happy([0, 1, 0, 1, 0]) ➞ 0
    
    portion_happy([0, 1, 1, 0]) ➞ 0.5
    
    portion_happy([0, 0, 0, 1, 1]) ➞ 1
    
    portion_happy([1, 0, 0, 1, 1]) ➞ 0.8

### Notes

  * Remember: a `0` border number is unhappy if its only neighbor is a `1` and vice versa.
  * A list will contain at least two elements.

"""

from functools import reduce
def happy(l):
  res = (1 if l[0] == l[1] else 0) + (1 if l[-1] == l[-2] else 0)
  print(res)
  #print([(i,x) for i,x in filter(lambda x: x[0] != 0 and x[0] != len(l)-1,enumerate(l))])
  res += reduce(lambda a,b:a + 1 if l[b[0]] == l[b[0]-1] or l[b[0]] == l[b[0]+1] else 0 ,filter(lambda x: x[0] != 0 and x[0] != len(l)-1,enumerate(l)),0)
  #print(res)
  return res  
    
def portion_happy(numbers):
  hap = happy(numbers)
  #print(hap,len(numbers)-hap)
  return happy(numbers)/(len(numbers))
print(percentage_happy([1, 0, 0, 1, 1]))

