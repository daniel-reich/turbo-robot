"""


Create a function that _counts_ the integer's **number of digits**.

### Examples

    count(318) ➞ 3
    
    count(-92563) ➞ 5
    
    count(4666) ➞ 4
    
    count(-314890) ➞ 6
    
    count(654321) ➞ 6
    
    count(638476) ➞ 6

### Notes

  * Solve this **without using strings**.
  * Alternatively, you can solve this via a _recursive approach_.
  * A _recursive_ version of this challenge can be found via this [link](https://edabit.com/challenge/ntJXZh4W8khX9nLPG).

"""

def count(n):
  n = str(n)
  output = 0
  for i in n:
    if i.isdigit():
      output+= 1
  return output

