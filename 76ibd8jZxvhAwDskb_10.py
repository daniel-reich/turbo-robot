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

def tallest_skyscraper(list_array):
  city_length = len(list_array[0])
  buildings = {}
  for i in range(city_length):
    height = 0
    for level in list_array:
      height += level[i]
    buildings[i] = height
​
  highest_building = 0
  max_height = 0 
  for building, height in buildings.items():
    if height > max_height:
      highest_building = building
      max_height = height
​
  return max_height

