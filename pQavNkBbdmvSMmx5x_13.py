"""


Create a function that returns the **majority vote** in a list. A majority
vote is an element that occurs **> N/2** times in a list (where **N** is the
length of the list).

### Examples

    majority_vote(["A", "A", "B"]) ➞ "A"
    
    majority_vote(["A", "A", "A", "B", "C", "A"]) ➞ "A"
    
    majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None

### Notes

  * The frequency of the majority element must be **strictly greater** than 1/2.
  * If there is no majority element, return `None`.
  * If the list is empty, return `None`.

"""

import numpy as np
def majority_vote(lst):
  length_of_list = len(lst)
  uniq_list= np.unique(lst)
  for x in uniq_list:
    if lst.count(x) > length_of_list/2:
      return x

