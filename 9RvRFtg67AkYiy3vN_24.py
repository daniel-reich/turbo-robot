"""


Create a **left rotation** and a **right rotation** function that returns all
the left rotations and right rotations of a string.

### Examples

    left_rotations("abc") ➞ ["abc", "bca", "cab"]
    
    right_rotations("abc") ➞ ["abc", "cab", "bca"]
    
    left_rotations("abcdef")
    ➞ ["abcdef", "bcdefa", "cdefab", "defabc", "efabcd", "fabcde"]
    
    right_rotations("abcdef")
    ➞ ["abcdef", "fabcde", "efabcd", "defabc", "cdefab", "bcdefa"]

### Notes

N/A

"""

def left_rotations(txt):
  t_str = txt
  t_list= []
  for i in range(len(txt)):
    t_list.append(t_str)
    t_str = t_str + t_str[0]
    t_str = t_str[1:]
  return t_list
​
​
def right_rotations(txt):
  t_str = txt
  t_list= []
  for i in range(len(txt)):
    t_list.append(t_str)
    t_str = t_str[-1] + t_str 
    t_str = t_str[:-1]
  return t_list

