"""


I have a bucket containing an amount of navy blue paint and I'd like to paint
as many walls as possible. Create a function that returns the number of
**complete walls** that I can paint, before I need to head to the shops to buy
more.

  * `n` is the number of square meters I can paint.
  * `w` and `h` are the widths and heights of a single wall in meters.

### Examples

    how_many_walls(100, 4, 5) ➞ 5
    
    how_many_walls(10, 15, 12) ➞ 0
    
    how_many_walls(41, 3, 6) ➞ 2

### Notes

  * Don't count a wall if I don't manage to finish painting all of it before I run out of paint.
  * All walls will have the same dimensions.
  * All numbers will be positive integers.

"""

def how_many_walls(n, w, h):
  return int(n / (w * h))

