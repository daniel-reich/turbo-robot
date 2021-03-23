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

def classify_rug(pattern):
    h = horizontal_check(pattern)
    v = vertical_check(pattern)
    if h and v:
        return 'perfect'
    elif h:
        return 'horizontally symmetric'
    elif v:
        return 'vertically symmetric'
    else:
        return 'imperfect'
​
​
​
def horizontal_check(pattern):
    if len(pattern) % 2 == 0:
        #dont do any operations on the division by 2
        if sorted([x for x in pattern[0:len(pattern)//2]]) == sorted([x for x in pattern[len(pattern)//2:]]):
            return True
        else:
            return False
​
    elif len(pattern) % 2 != 0:
        pattern.pop((len(pattern)-1)//2)
        return horizontal_check(pattern)
​
​
def vertical_check(pattern):
    
    try:
        len(pattern[0])
    except:
        return True
        
    if len(pattern[0]) % 2 == 0:
        if sorted([ row[0:len(row)//2] for row in pattern  ]) == sorted([ row[len(row)//2:] for row in pattern]):
            return True
        else:
            return False
​
    elif len(pattern[0]) % 2 != 0:
        popping = (len(pattern[0]) - 1) //2
        for x in range(len(pattern)):
            pattern[x].pop(popping)
        return vertical_check(pattern)

