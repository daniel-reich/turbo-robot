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

def lcm(nums):
  answer = 1
  for i in nums:  
      answer = int((answer * i)/gcd(answer, i)) 
  return answer
      
def gcd(a,b):
  return a if(b==0) else gcd(b,a%b)

