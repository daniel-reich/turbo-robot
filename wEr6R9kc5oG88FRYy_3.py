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
  if w < 3 or h < 3:
    return "invalid"
  matrix = []
  matrix.append([w * ch])
  for i in range(h-2):
    matrix.append([ch + ((w-2) * " ") + ch])
  matrix.append([w * ch])
  return matrix

