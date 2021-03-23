"""


A square matrix (same number of rows as columns) is called _row diagonally
dominant_ if "the absolute value of each entry in the main diagonal is
strictly larger than the sum of the absolute values of the other entries in
that row".

To illustrate ...

    [
      [10, 3, 6],
      [2, -9, -6],
      [1, -1, 4]
    ]

The absolute values from top left to bottom right are:

  * `10` = First item of first row.
  * `9` = Second item of second row.
  * `4` = Third item of third row.

... making a _row diagonal dominant_ total of 23.

 **In the first row ...**

  * The value of the _row diagonal dominant_ is `10`.
  * The sum of the other absolute values are `3` and `6` make a total of `9`.

... so far, the matrix is _row diagonally dominant_ , since `10 > 9`.

 **In the second row ...**

  * The value of the _row diagonal dominant_ is `9`.
  * The sum of the other absolute values in the second row are `3` and `6` which make a total of `9`.

... meaning the matrix is not _row diagonally dominant_ since `9 <= 9`.

    [
      [10, 3, 6],
      [3, -9, -6],
      [1, -1,  4]
    ]

For a square to be _row diagonally dominant_ , all of the rows in the square
have to be like Row 1.

Write a function that determines if a given square matrix is row diagonally
dominant.

### Examples

    diag_dom([
      [2, -1],
      [-1, 2]
    ]) ➞ True
    
    diag_dom([
      [0, 1],
      [1, 0]
    ]) ➞ False
    
    diag_dom([
      [10, 3, 6],
      [2, -9, -6],
      [1, -1, 4]
    ]) ➞ True
    
    diag_dom([
      [10, 3, 6],
      [4, -9, -6],
      [1, -1, 4]
    ]) ➞ False

### Notes

As in the examples, the size of the matrices will change, but they will always
be square.

"""

def diag_dom(arr):
  return all(abs(arr[i][i]) > sum(abs(n) for n in arr[i])-abs(arr[i][i]) for i in range(len(arr)))

