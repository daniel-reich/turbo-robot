"""


A city skyline can be represented as a 2-D list with `1`s representing
buildings. In the example below, the height of the tallest building is **4**
(second-most right column).

    [[0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1]]

Create a function that takes a **skyline** (2-D list of 0's and 1's) and
returns the height of the tallest skyscraper.

### Examples

    tallest_skyscraper([
      [0, 0, 0, 0],
      [0, 1, 0, 0],
      [0, 1, 1, 0],
      [1, 1, 1, 1]
    ]) ➞ 3
    
    tallest_skyscraper([
      [0, 1, 0, 0],
      [0, 1, 0, 0],
      [0, 1, 1, 0],
      [1, 1, 1, 1]
    ]) ➞ 4
    
    tallest_skyscraper([
      [0, 0, 0, 0],
      [0, 0, 0, 0],
      [1, 1, 1, 0],
      [1, 1, 1, 1]
    ]) ➞ 2

### Notes

N/A

"""

def tallest_skyscraper(lst):
  for i in range(len(lst)):
    if sum(lst[i]) > 0:
      return (len(lst) - i)

