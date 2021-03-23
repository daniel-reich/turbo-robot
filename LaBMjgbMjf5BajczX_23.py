"""


Write a function that counts how many concentric layers a rug.

### Examples

    count_layers([
      "AAAA",
      "ABBA",
      "AAAA"
    ]) ➞ 2
    
    count_layers([
      "AAAAAAAAA",
      "ABBBBBBBA",
      "ABBAAABBA",
      "ABBBBBBBA",
      "AAAAAAAAA"
    ]) ➞ 3
    
    count_layers([
      "AAAAAAAAAAA",
      "AABBBBBBBAA",
      "AABCCCCCBAA",
      "AABCAAACBAA",
      "AABCADACBAA",
      "AABCAAACBAA",
      "AABCCCCCBAA",
      "AABBBBBBBAA",
      "AAAAAAAAAAA"
    ]) ➞ 5

### Notes

  * Multiple layers can share the **same component** so count them separately (example #2).
  * Layers will be horizontally and vertically symmetric.
  * There will be at least one layer for each rug.

"""

def count_layers(rug):
    count = 1
    val1 = len(rug)
    q1 = val1//2
    val2 = len(rug[q1])
    q2 = val2//2
    for i in range(q2):
        if rug[q1][i] != rug[q1][i+1]:
            count = count + 1
    return(count)

