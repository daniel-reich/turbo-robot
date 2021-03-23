"""


Given a Rubik's Cube with a side length of `n`, return the number of
individual stickers that are needed to cover the whole cube.

![Pictures of Rubik's Cubes](https://edabit-
challenges.s3.amazonaws.com/rubrix.png)

  * The Rubik's cube of side length `1` has **6 stickers**.
  * The Rubik's cube of side length `2` has **24 stickers**.
  * The Rubik's cube of side length `3` has **54 stickers**.

### Examples

    how_many_stickers(1) ➞ 6
    
    how_many_stickers(2) ➞ 24
    
    how_many_stickers(3) ➞ 54

### Notes

  * Keep in mind there are six faces to keep track of.
  * Expect only positive whole numbers.

"""

def how_many_stickers(n):
  return 6 * (n**2)

