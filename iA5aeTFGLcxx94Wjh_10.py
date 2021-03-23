"""


Create a function that takes two arguments: a list `lst` and a number `num`.
If an element occurs in `lst` more than `num` times, remove the extra
occurrence(s) and return the result.

### Examples

    delete_occurrences([1, 1, 1, 1], 2) ➞ [1, 1]
    
    delete_occurrences([13, True, 13, None], 1) ➞ [13, True, None]
    
    delete_occurrences([True, True, True], 3) ➞ [True, True, True]

### Notes

Do not alter the order of the original list.

"""

def delete_occurrences(mylist, num):
  from collections import Counter 
  mylist = list(reversed(mylist))
  counter_list = Counter(mylist)
  for variables in counter_list:
    if counter_list[variables] >= num: 
      for i in range(0, counter_list[variables]-num):
        del(mylist[mylist.index(variables)])
  return list(reversed(mylist))

