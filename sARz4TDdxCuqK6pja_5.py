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

import copy
def deadly_virus(persons, n):
    dict = {}
    for y in range(len(persons)):
        for x in range(len(persons[y])):
            dict[(y,x)] = persons[y][x]
​
    for i in range(n):
        temp = copy.deepcopy(persons)
        for y in range(len(persons)):
            for x in range(len(persons[y])):
                if (y-1,x) in dict:
                    if persons[y-1][x] == 'V':
                        temp[y][x] = 'V'
                if (y+1,x) in dict:
                    if persons[y+1][x] == 'V':
                        temp[y][x] = 'V'
                if (y,x-1) in dict:
                    if persons[y][x-1] == 'V':
                        temp[y][x] = 'V'
                if (y,x+1) in dict:
                    if persons[y][x+1] == 'V':
                        temp[y][x] = 'V'
        persons = copy.deepcopy(temp)
​
    return persons

