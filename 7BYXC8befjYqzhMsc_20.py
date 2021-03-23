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

def hs(rows):
  for i in range(len(rows) // 2):
    if rows[i] != rows[len(rows) - i - 1]: return False
  return True
def classify_rug(pattern):
  h, v = hs(pattern), hs(list(zip(*pattern)))
  if h and v: return "perfect"
  if h: return "horizontally symmetric"
  if v: return "vertically symmetric"
  return "imperfect"

