"""


 **Hamming distance** is the number of characters that differ between two
strings.

To illustrate:

    String1: "abcbba"
    String2: "abcbda"
    
    Hamming Distance: 1 - "b" vs. "d" is the only difference.

Create a function that computes the **hamming distance** between two strings.

### Examples

    hamming_distance("abcde", "bcdef") ➞ 5
    
    hamming_distance("abcde", "abcde") ➞ 0
    
    hamming_distance("strong", "strung") ➞ 1

### Notes

Both strings will have the same length.

"""

def hamming_distance(txt1, txt2):
  hamming = 0
  for x in range (0, len(txt1)):
    if txt1[x] != txt2[x]:
      hamming+= 1
  return hamming

