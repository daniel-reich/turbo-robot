"""


 **Mubashir** needs your help to identify the spread of a deadly virus. He can
provide you with the following parameters:

  * A two-dimensional array `persons`, containing **affected persons 'V'** and **unaffected persons 'P'**.
  * Number of hours `n`, each infected person is spreading the virus to one person _up, down, left and right_ **each hour**.

Your function should return the updated array containing affected and
unaffected persons after `n` hours.

### Examples

    persons = [
      ["P", "P", "P", "P", "P"],
      ["V", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"]
    ]
    deadly_virus(persons, 0) ➞ [
      ["P", "P", "P", "P", "P"],
      ["V", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"]
    ]
    
    deadly_virus(persons, 1) ➞ [
      ["V", "P", "P", "P", "P"],
      ["V", "V", "P", "P", "P"],
      ["V", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"]
    ]
    
    deadly_virus(persons, 2) ➞ [
      ["V", "V", "P", "P", "P"],
      ["V", "V", "V", "P", "P"],
      ["V", "V", "P", "P", "P"],
      ["V", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"]
    ]

### Notes

N/A

"""

def deadly_virus(persons, n):
  while n:
    persons = update(spread(infected(persons)))
    n -= 1
  return persons
​
def infected(matrix):
  result = []
  for index, row in enumerate(matrix):
    for i, person in enumerate(row):
      if person == 'V':
        result.append((index, i))
  return result
  
def spread(lst):
  result = []
  for (x, y) in lst:
    new = ((x+1, y), (x-1, y), (x, y+1), (x, y-1))
    for (a, b) in new:
      if a >= 0 and a <= 5 and b >=0 and b <= 5:
        result.append((a, b))
  result.extend(lst)
  return result
  
def update(lst):
  return [
    ['V' if (index, i) in lst else 'P' for i in range(5)]
    for index in range(5)
  ]

