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
    count = 0
    indexes = []
    for i in range(n):
        for j in range(len(persons)):
            for i in range(len(persons[i])):
                if persons[i][j] == 'V':
                    indexes.append((i,j))
        for x,y in indexes:
            try:
                ##above
                if x-1 == -1:
                    pass
                else:
                    persons[x-1][y] = 'V'
            except IndexError as err:
                pass
            try:
                ##below
                persons[x+1][y] = 'V'
            except IndexError as err:
                pass
            try:
                ##left
                if y-1 == -1:
                    pass
                else:
                    persons[x][y-1] = 'V'
            except IndexError as err:
                pass
            try:
                ##right
                indexes = []
                persons[x][y+1] = 'V'
            except IndexError as err:
                pass
    return persons

