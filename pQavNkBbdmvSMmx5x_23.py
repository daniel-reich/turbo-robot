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

def majority_vote(lst):
  unique=list(set(lst))
  if len(unique) == 1: return lst[0]
  if len(unique) == 0: return None
  unique_count=[]
  for i in range(len(unique)):
    unique_count.append(lst.count(unique[i]))
    sorted_list=sorted(unique_count, reverse=True)
  if sorted_list[0] == sorted_list[1]: return None
  local_max=max(unique_count)
  index=unique_count.index(max(unique_count))
  return unique[index]

