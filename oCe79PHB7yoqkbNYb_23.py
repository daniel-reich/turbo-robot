"""
A number has a **breakpoint** if it can be split in a way where the digits on
the left side and the digits on the right side sum to the same number.

For instance, the number _35190_ can be sliced between the digits _351_ and
_90_ , since _3 + 5 + 1 = 9_ and _9 + 0 = 9_. On the other hand, the number
_555_ does **not** have a **breakpoint** (you must split **between** digits).

Create a function that returns `True` if a number has a breakpoint, and
`False` otherwise.

### Examples

    break_point(159780) ➞ True
    
    break_point(112) ➞ True
    
    break_point(1034) ➞ True
    
    break_point(10) ➞ False
    
    break_point(343) ➞ False

### Notes

  * Read each digit as only one number.
  * Check the **Resources** tab for a hint.

"""

def break_point(num):
 output=False
 num_str=str(num)
 # go through string
 for i in range(0,len(num_str)):
  sum_left=0
  sum_right=0
  # create sums left and right of index
  for l in range(0,i):
   sum_left+=int(num_str[l])
  #print(sum_left)
  for r in range(i,len(num_str)):
   sum_right+=int(num_str[r])
  #print(sum_right)
  if sum_left == sum_right:
   output=True
   break
 return output

