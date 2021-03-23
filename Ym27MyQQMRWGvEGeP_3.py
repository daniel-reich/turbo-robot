"""


Write a function that will return `True` if a given string (divided and
grouped into a size) will contain a set of **consecutive** numbers (regardless
of orientation: whether **ascending** or **descending** ), otherwise, return
`False`.

### IMPORTANT

The expected solution for this challenge is done **recursively**. Please check
out the **Resources** tab for more details about **recursion** in Java.

### Examples

    is_consecutive("121314151617") ➞ True
    # Contains a set of consecutive ascending numbers
    # if grouped into 2's : 12, 13, 14, 15, 16, 17
    
    is_consecutive("123124125") ➞ True
    # Contains a set of consecutive ascending numbers
    # if grouped into 3's : 123, 124, 125
    
    is_consecutive("32332432536") ➞ False
    # Regardless of the grouping size, the numbers can't be consecutive.
    
    is_consecutive("326325324323") ➞ True
    # Contains a set of consecutive descending numbers
    # if grouped into 3's : 326, 325, 324, 323
    
    is_consecutive("667666") ➞ True
    # Consecutive descending numbers: 667 and 666.
    
    is_consecutive("999897959493") ➞ False

### Notes

  * A **number** can consist of any number of digits, so long as the numbers are **adjacent** to each other, and the string has **at least two** of them.
  * An **iterative** version of this challenge can be found via this [link](https://edabit.com/challenge/eHwd6medMrY3QXM8k).

"""

def is_consecutive(s):
  def group_by_size(string, size):
    if len(string) == size:
      return [string]
    elif len(string) < size:
      return ['X']
    else:
      return [string[:size]] + group_by_size(string[size:], size)
  def consecutive(group, index = 0, previous = None, direct = None):
    if previous == None:
      previous = int(group[index])
      return consecutive(group, index+1, previous)
    else:
      if index == len(group):
        return True
      elif direct == None:
        if int(group[index]) not in [previous - 1, previous + 1]:
          return False
        elif int(group[index]) == (previous - 1):
          direct = 'd'
        else:
          direct = 'a'
        
        return consecutive(group, index+1, int(group[index]), direct)
      else:
        if direct == 'a':
          if int(group[index]) != previous + 1:
            return False
          else:
            return consecutive(group, index+1, int(group[index]), direct)
        else:
          if int(group[index]) != previous - 1:
            return False
          else:
            return consecutive(group, index+1, int(group[index]), direct)
  
  valid_groups = [group_by_size(s,n) for n in range(1, len(s) // 2 + 1) if 'X' not in group_by_size(s,n)]
  consecs = [consecutive(group) for group in valid_groups]
  print(s)
  return True in consecs

