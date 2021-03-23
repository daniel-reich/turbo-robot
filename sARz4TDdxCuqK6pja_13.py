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
  for hours in range(n):
      coordinates = []
      for sublistindex in range(len(persons)):
          if "V" in persons[sublistindex]:
              for position in range(len(persons[sublistindex])):
                  if persons[sublistindex][position] == "V":
                      coordinates.append([sublistindex, position])
​
      for coordpair in coordinates:
          try:
              if coordpair[0] == 0:
                  persons[coordpair[0] + 1][coordpair[1]] = "V"
              else:
                  persons[coordpair[0] - 1][coordpair[1]] = "V"
                  persons[coordpair[0] + 1][coordpair[1]] = "V"
              if coordpair[1] == 0:
                  persons[coordpair[0]][coordpair[1] + 1] = "V"
              else:
                  persons[coordpair[0]][coordpair[1] - 1] = "V"
                  persons[coordpair[0]][coordpair[1] + 1] = "V"
          except:
              print("wrong")
​
  return persons

