"""


Create a function that counts the number of towers.

### Examples

    count_towers([
      ["     ##         "],
      ["##   ##        ##"],
      ["##   ##   ##   ##"],
      ["##   ##   ##   ##"]
    ]) ➞ 4
    
    count_towers([
      ["                         ##"],
      ["##             ##   ##   ##"],
      ["##        ##   ##   ##   ##"],
      ["##   ##   ##   ##   ##   ##"]
    ]) ➞ 6
    
    count_towers([
      ["##"],
      ["##"]
    ]) ➞ 1

### Notes

  * You are given a 2D matrix.
  * Towers are two characters in length.
  * Towers are made only of the character **#**.
  * Some tests have no towers, return `0`.

"""

def count_towers(towers):
  if len(towers[-1][0])==0:
    return 0
  return sum(1 for i in towers[-1][0].split('  '))

