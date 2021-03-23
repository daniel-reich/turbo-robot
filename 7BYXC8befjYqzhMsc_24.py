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

def classify_rug(arr):
    horizontal = True
    vertical = True
    # sudah pasti perfect jika 1x1
    if len(arr) == 1 and len(arr[0]) == 1:
        return "perfect"
​
    isi_ver = [""] * len(arr)
    isi_hor = [""] * len(arr[0])
​
    # looping untuk verti
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            isi_ver[x] += arr[x][y]
        # cek si vertical
        if isi_ver[x] != isi_ver[x][::-1]:
            vertical = False
​
    # looping untuk hori
    for y in range(len(arr[0])):
        for x in range(len(arr)):
            isi_hor[y] += arr[x][y]
        # cek si hori
        if isi_hor[y] != isi_hor[y][::-1]:
            horizontal = False
​
    if horizontal == True and vertical == False:
        return "horizontally symmetric"
    elif horizontal == False and vertical == True:
        return "vertically symmetric"
    elif horizontal and vertical:
        return "perfect"
    else:
        return "imperfect"
​
print(classify_rug([
    ["a", "a", "a", "a"],
    ["d", "a", "a", "a"],
]))

