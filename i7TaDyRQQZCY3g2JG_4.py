"""


Given a list of integers, create a function that will find the **smallest**
positive integer that is evenly divisible by all the members of the list. In
other words, find the least common multiple (LCM).

### Examples

    lcm([1, 2, 3, 4, 5, 6, 7, 8, 9]) ➞ 2520
    
    lcm([5]) ➞ 5
    
    lcm([5, 7, 11]) ➞ 385
    
    lcm([5, 7, 11, 35, 55, 77]) ➞ 385

### Notes

N/A

"""

def lcm(arr):
  if len(arr)==1: return arr[0]
  gcd = lambda a,b: a if not b else gcd(b, a%b)
  results = arr[0]*arr[1]//gcd(arr[0],arr[1])
  for x in arr[2:]: results = results*x//gcd(results,x)
  return results

