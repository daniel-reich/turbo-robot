"""


Given three groups of numbers, return a list containing all numbers that
appear in more than one group (in ascending order).

### Examples

    number_groups([7, 8, 7, 3, 4], [2, 9, 1, 2, 1], [5, 6, 6, 6, 5]) ➞ []
    
    number_groups([3, 8, 8, 1, 1], [9, 1, 1, 9, 9], [10, 7, 6, 6, 3]) ➞ [1, 3]
    
    number_groups([4, 10, 9, 2, 2], [5, 3, 7, 3, 8], [6, 2, 9, 4, 2]) ➞ [2, 4, 9]
    
    number_groups([7, 8, 4, 8, 7], [8, 5, 9, 2, 9], [6, 1, 5, 5, 6]) ➞ [5, 8]

### Notes

N/A

"""

def number_groups(group1, group2, group3):
  sg1 = list(set(group1))
  sg2 = list(set(group2))
  sg3 = list(set(group3))
  
  return sorted(set([i for i in sg1 if i in sg2 or i in sg3 ] + [i for i in sg2 if i in sg3]))

