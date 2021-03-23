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
    k = []
    for i in towers:
        j = i[0].split()
        le = len(j)
        k.append(le)
    return max(k)

