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

def classify_rug(l):
    print(l)
    rows = len(l)
    cols = len(l[0])
    if cols ==1 and rows==1:
        return "perfect"
    c = [list(x) for x in zip(*l)]
    ver, hor = True, True
    for i in range(int(rows // 2)):
        if l[0 + i] != l[-1 - i]:
            hor = False
            break
    print()
    for i in range(int(cols // 2)):
        if c[0 + i] != c[-1 - i]:
            ver = False
            break
    if ver and hor:
        out = "perfect"
    elif not ver and not hor:
        out = "imperfect"
    elif ver and not hor:
        out = "vertically symmetric"
    elif hor and not ver:
        out = "horizontally symmetric"
    return out

