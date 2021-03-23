"""


Write a function that, given the start `start_num` and end `end_num` values,
return a list containing all the numbers **inclusive** to that range. See
examples below.

### Examples

    inclusive_list(1, 5) ➞ [1, 2, 3, 4, 5]
    
    inclusive_list(2, 8) ➞ [2, 3, 4, 5, 6, 7, 8]
    
    inclusive_list(10, 20) ➞ [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    
    inclusive_list(17, 5) ➞ [17]

### Notes

  * The numbers in the list are sorted in ascending order.
  * If `start_num` is greater than `end_num`, return a list with the higher value. See example #4.
  * A recursive version of this of challenge can be found [here](https://edabit.com/challenge/CoSFaDzSxrSjsZ8F6).

"""

def inclusive_list(start_num, end_num):
  if end_num <= start_num:
    return [start_num]
  else:
    return [i for i in range(start_num, end_num+1)]

