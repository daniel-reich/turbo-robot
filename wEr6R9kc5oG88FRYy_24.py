"""


Create a function that takes the **width** , **height** and **character** and
returns a picture frame as a 2D list.

### Examples

    get_frame(4, 5, "#") ➞ [
      ["####"],
      ["#  #"],
      ["#  #"],
      ["#  #"],
      ["####"]
    ]
    # Frame is 4 characters wide and 5 characters tall.
    get_frame(10, 3, "*") ➞ [
      ["**********"],
      ["*        *"],
      ["**********"]
    ]
    # Frame is 10 characters and wide and 3 characters tall.
    get_frame(2, 5, "0") ➞ "invalid"
    # Frame's width is not more than 2.

### Notes

  * Remember the gap.
  * Return `"invalid"` if **width** or **height** is _2 or less_ (can't put anything inside).

"""

def get_frame(w, h, ch):
  first = ""
  middle = ""
  if w <= 2 or h <= 2:
    return "invalid"
  
  for each in range(w):
    first += ch
    if each > 0 and each < w - 1:
      middle += " "
    else:
      middle += ch
  first = [first]
  middle = [middle]
  arr = []
  arr.append(first)
  for each in range(1, h - 1):
    arr.append(middle)
  arr.append(first)
  return arr

