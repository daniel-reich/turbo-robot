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
   
   cnt = 0
   lenLst = len(lst)
   temp = 0
   val = None
   for cnt  in range(lenLst):
       n =  majority_vote_helper(lst, cnt) 
       if n > lenLst/2:
            if n > temp:
               temp = n
               val = lst[cnt]
       cnt = cnt + 1
   return val   
        
def majority_vote_helper(lst, p):
    cnt = 0
    for x in lst:
        if x == lst[p]:
             cnt = cnt+1
        else:
           cnt = cnt
    return cnt
majority_vote(["A", "A", "A", "B", "C", "A"])

