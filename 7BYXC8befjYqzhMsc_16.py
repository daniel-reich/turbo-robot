"""


Kathleen owns a beautiful rug store. She likes to group the rugs into 4
mutually exclusive categories.

  * imperfect
  * horizontally symmetric
  * vertically symmetric
  * perfect

An **imperfect** rug is one that is **neither horizontally nor vertically
symmetric**. Here is an example of an **imperfect** rug:

    [
      ["a", "a", "a", "a"],
      ["a", "a", "a", "a"],
      ["a", "a", "b", "b"]
    ]

The following is an **horizontally symmetric** rug. You could "fold" the rug
across a hypothetical x-axis, and both sides would be identical. A
horizontally symmetric rug is **not** vertically symmetric (otherwise this rug
would be classified as **perfect** ).

    [
      ["c", "a", "a", "a"],
      ["b", "b", "b", "b"],
      ["c", "a", "a", "a"]
    ]

The following is a **vertically symmetric** rug. You could "fold" the rug
across a hypothetical y-axis, and both sides would be identical. A vertically
symmetric is **not** horizontally symmetric (otherwise this rug would be
classified as **perfect** ).

    [
      ["a", "b", "a"],
      ["b", "b", "b"],
      ["a", "b", "a"],
      ["a", "b", "a"]
    ]

Finally, a **perfect** rug is one that is **both vertically and horizontally
symmetric**. That is, folded either length-wise or width-wise will yield two
identical pieces.

    [
      ["a", "b", "b", "a"],
      ["b", "b", "b", "b"],
      ["a", "b", "b", "a"]
    ]

Given a rug of `m x n` dimension, determine whether it is **imperfect,
horizontally symmetric, vertically symmetric or perfect**. Rugs are
represented using a two-dimensional list.

### Examples

    classify_rug([
      ["a", "a"],
      ["a", "a"]
    ]) ➞ "perfect"
    
    classify_rug([
      ["a", "a", "b"],
      ["a", "a", "a"],
      ["b", "a", "a"]
    ]) ➞ "imperfect"
    
    classify_rug([
      ["b", "a"],
      ["b", "a"]
    ]) ➞ "horizontally symmetric"
    
    classify_rug([
      ["a", "a"],
      ["b", "b"]
    ]) ➞ "vertically symmetric"

### Notes

You can consider a `1 x n` rug as being trivially **horizontally symmetric** ,
an `n x 1` rug as being trivially **vertically symmetric** , and a `1 x 1` rug
as being trivially **perfect**.

"""

def list_shape(lst):
    if type(lst[0]) is list:
        return(len(lst[0]), len(lst))
    else:
        return (len(lst), 1)
​
​
def classify_rug(pattern):
    horzSym = False
    vertSym = False
​
    dim = list_shape(pattern)
    # Check horizontal symmetry
    if dim[1] == 1:
        horzSym = True
    else:
        x = 0
        checking = True
        while x < dim[0] and checking:
            y = 0
            while y < dim[1]/2 and checking:
                if pattern[y][x] != pattern[dim[1] - y - 1][x]:
                    checking = False
                    horzSym = False
                    break
                else:
                    horzSym = True
                y += 1
            x += 1
​
    # Check vertical symmetry
    if dim[0] == 1:
        vertSym = True
    else:
        y = 0
        checking = True
        while y < dim[1] and checking:
            x = 0
            while x < dim[0] / 2 and checking:
                if pattern[y][x] != pattern[y][dim[0] - x - 1]:
                    checking = False
                    vertSym = False
                    break
                else:
                    vertSym = True
                x += 1
            y += 1
​
    # Classify based on results
    if horzSym and vertSym:
        return "perfect"
    elif horzSym:
        return "horizontally symmetric"
    elif vertSym:
        return "vertically symmetric"
    else:
        return "imperfect"

