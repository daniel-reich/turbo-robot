"""


Create a function that receives a square n*n matrix and returns that matrix
after it has been rotated 90 degrees in the clockwise direction.

### Examples

    rotate([
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]) ➞ [
      [7, 4, 1],
      [8, 5, 2],
      [9, 6, 3]
    ]
    
    rotate([
      ["a", "b", "c", "d"],
      ["e", "f", "g", "h"],
      ["i", "j", "k", "l"],
      ["m", "n", "o", "p"]
    ]) ➞ [
      ["m", "i", "e", "a"],
      ["n", "j", "f", "b"],
      ["o", "k", "g", "c"],
      ["p", "l", "h", "d"]
    ]

### Notes

N/A

"""

def rotate(mat):
  outputlist = [[] for sublist in mat]
​
  elementcount = 0
  for sublist in mat:
      for element in sublist:
          elementcount += 1
  indexcount = len(mat) - 1
  check = 0
​
  templist = []
  for number in range(1, elementcount + 1):
      if number % len(mat) == 0:
          templist.append(number)
​
  for number in range(1, elementcount + 1):
      if number in templist:
          outputlist[check].append(mat[indexcount].pop(0))
          indexcount = len(mat) - 1
          check += 1
      else:
          outputlist[check].append(mat[indexcount].pop(0))
          indexcount -= 1
​
  return outputlist

