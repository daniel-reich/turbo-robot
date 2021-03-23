"""


Given a list of lists, return a new list of lists containing every element,
**except for the outer elements**.

### Examples

    peel_layer_off([
      ["a", "b", "c", "d"],
      ["e", "f", "g", "h"],
      ["i", "j", "k", "l"],
      ["m", "n", "o", "p"]
    ]) ➞ [
      ["f", "g"],
      ["j", "k"]
    ]
    
    peel_layer_off([
      [1, 2, 3, 4, 5],
      [6, 7, 8, 9, 10],
      [11, 12, 13, 14, 15],
      [16, 17, 18, 19, 20],
      [21, 22, 23, 24, 25],
      [26, 27, 28, 29, 30],
      [31, 32, 33, 34, 35]
    ]) ➞ [
      [7, 8, 9],
      [12, 13, 14],
      [17, 18, 19],
      [22, 23, 24],
      [27, 28, 29]
    ]
    
    peel_layer_off([
      [True, False, True],
      [False, False, True],
      [True, True, True]
    ]) ➞ [[False]]
    
    peel_layer_off([
      ["hello", "world"],
      ["hello", "world"]
    ]) ➞ []

### Notes

  * The 2D grid is always a rectangular/square shape.
  * Always return some form of nested list, unless there are no elements. In that case, return an empty list.

"""

peel_layer_off=lambda l:[i[1:-1] for i in l][1:-1]

