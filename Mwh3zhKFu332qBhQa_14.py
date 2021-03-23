"""


 **Mubashir** is trying to figure out the corresponding quadratic formula for
the following quadratic sequence of numbers:

N| Result  
---|---  
1| 90  
2| 240  
3| 450  
4| 720  
5| 1050  
  
If you can figure this out, then help him by creating a function that takes a
number `n` and returns the **nth number of this quadratic sequence**.

### Examples

    guess_sequence(1) ➞ 90
    
    guess_sequence(2) ➞ 240
    
    guess_sequence(3) ➞ 450

### Notes

If you are not sure about how to find the formula of a quadratic sequence,
check the Resources.

"""

def guess_sequence(n):
  
  answer = 90
  addition = 150
  
  added = 1
  required = n
  
  while (added < required):
    answer += addition
    addition += 60
    added += 1
    
  return answer

