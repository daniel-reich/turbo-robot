"""


Create a function which converts an **ordered** number list into a list of
ranges (represented as strings). Note how some lists have some numbers
missing.

### Examples

    numbers_to_ranges([1, 2, 3, 4, 5]) ➞ ["1-5"]
    
    numbers_to_ranges([3, 4, 5, 10, 11, 12]) ➞ ["3-5", "10-12"]
    
    numbers_to_ranges([1, 2, 3, 4, 99, 100]) ➞ ["1-4", "99-100"]
    
    numbers_to_ranges([1, 3, 4, 5, 6, 7, 8]) ➞ ["1", "3-8"]

### Notes

  * If there are no numbers consecutive to a number in the list, represent it as only the _string_ version of that number (see example #4).
  * Return an empty list if the given list is empty.

"""

def numbers_to_ranges(lst):
  m=[]
  p=""
  f=[]
  if len(lst)==0:
    return []
  elif len(lst)==1:
    return [str(lst[0])]
  for l in range(len(lst)):
    if l==len(lst)-2:
      if lst[l]+1==lst[l+1]:
        m.append(lst[l])
        m.append(lst[l+1])
        p=str(min(m))+"-"+str(max(m))
        f.append(p)
        return f
      else:
        m.append(lst[l])
        if len(m)==1:
          p=str(m[0])
          f.append(p)
          p=""
        else:
          p=str(min(m))+"-"+str(max(m))
          f.append(p)
          p=""
        m.append(lst[l+1])
        p=str(m[0])
        f.append(p)
        return f
    if lst[l]+1==lst[l+1]:
      m.append(lst[l])
    else:
      m.append(lst[l])
      if len(m)==1:
        p=str(m[0])
        f.append(p)
        p=""
      else:
        p=str(min(m))+"-"+str(max(m))
        f.append(p)
        p=""
      m=[]

