"""


Write a function that pairs the first number in an array with the last, the
second number with the second to last, etc.

### Examples

    pairs([1, 2, 3, 4, 5, 6, 7]) ➞ [[1, 7], [2, 6], [3, 5], [4, 4]]
    
    pairs([1, 2, 3, 4, 5, 6]) ➞ [[1, 6], [2, 5], [3, 4]]
    
    pairs([5, 9, 8, 1, 2]) ➞ [[5, 2], [9, 1], [8, 8]]
    
    pairs([]) ➞ []

### Notes

  * If the list has an **odd length** , repeat the middle element twice for the last pair.
  * Return an empty list if the input is an empty list.

"""

def pairs(lst):
  if len(lst) % 2 == 0:
    listI = []
    for i in range(0,(len(lst) // 2)):
      listA = []
      listA.append(lst[i])
      listA.append(lst[len(lst) - (i + 1)])
      listI.append(listA)
    return listI
  else:
    listI = []
    midpoint = (len(lst)/2) - 0.5
    for i in range(0,(len(lst) // 2)+1):
      listA = []
      if i == midpoint:
        listA.append(lst[i])
        listA.append(lst[i])
        listI.append(listA)
      else:
        listA.append(lst[i])
        listA.append(lst[len(lst) - (i + 1)])
        listI.append(listA)
    return listI

