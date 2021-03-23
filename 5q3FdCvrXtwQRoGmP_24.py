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
  tower_count =0
  for tower in towers:
    if len(tower[0].replace(' ', '')) >= tower_count:
      tower_count = len(tower[0].replace(' ', ''))
    if tower_count != 0:
      tower_count = tower_count/2
​
  return tower_count

