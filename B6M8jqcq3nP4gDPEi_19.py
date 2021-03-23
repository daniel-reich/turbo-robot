"""


Write a function that extracts the max value of a number in a list. If there
are **two or more** max values, return it **as a list** , otherwise, return
the **number**. This process could be relatively easy with some of the built-
in list functions but the required approach is **recursive**.

### Examples

    iso_group([31, 7, 2, 13, 7, 9, 10, 13]) ➞ 31
    
    iso_group([1, 3, 9, 5, 1, 7, 9, -9]) ➞ [9, 9]
    
    iso_group([97, 19, -18, 97, 36, 23, -97]) ➞ [97, 97]
    
    iso_group([-31, -7, -13, -7, -9, -13]) ➞ [-7, -7]
    
    iso_group([-1, -3, -9, -5, -1, -7, -9, -9]) ➞ [-1, -1]
    
    iso_group([107, 19, -18, 79, 36, 23, 97]) ➞ 107

### Notes

You can read more about recursion (see the **Resources** tab) if you aren't
familiar with it yet or haven't fully understood the concept before taking up
this challenge.

"""

def iso_group(lst):
  # your recursive solution here
  if lst[0] != "potato":
    lst = ["potato", lst[0] - 1, 0, 0] + lst
  else:
    i = lst[2] + 4
    if i < len(lst):    
      if lst[i] > lst[1]:
        lst[3] = 1
        lst[1] = lst[i]
      elif lst[i] == lst[1]:
        lst[3] += 1
      lst[2] += 1
    else:
      if lst[3] == 1:
        return lst[1]
      else:
        return [lst[1]]*lst[3]
  return iso_group(lst)

