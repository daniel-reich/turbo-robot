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
  for vote in set(lst):
    if lst.count(vote) > len(lst)/2:
      return vote
  return None

