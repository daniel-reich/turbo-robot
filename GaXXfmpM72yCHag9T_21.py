"""


Create a function that takes a list of numbers and return the number that's
unique.

### Examples

    unique([3, 3, 3, 7, 3, 3]) ➞ 7
    
    unique([0, 0, 0.77, 0, 0]) ➞ 0.77
    
    unique([0, 1, 1, 1, 1, 1, 1, 1]) ➞ 0

### Notes

Test cases will always have exactly one unique number while all others are the
same.

"""

def unique(lst):
  lst.sort()
  hlp=len(lst)-2
  for i in range(1,len(lst)-1):
    item_prev=lst[i-1]
    item_now=lst[i]
    item_next=lst[i+1]
    if(item_prev!=item_now and item_now!=item_next):
      return item_now
    if(i==hlp and item_now!=item_next):
      return item_next
    if(item_prev!=item_now and item_now==item_next and i==1):
      return item_prev

