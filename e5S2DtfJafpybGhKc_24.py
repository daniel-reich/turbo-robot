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

def rotate(mat: list):
  return list(map(list, map(reversed, zip(*mat))))

