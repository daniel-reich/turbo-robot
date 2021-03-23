"""


Given two words, the **letter distance** is calculated by taking the absolute
value of the difference in character codes and summing up the difference.

If one word is longer than another, add the difference in lengths towards the
score.

To illustrate:

    letter_distance("house", "fly") = dist("h", "f") + dist("o", "l") + dist("u", "y") + dist(house.length, fly.length)
    
    = |104 - 102| + |111 - 108| + |117 - 121| + |5 - 3|
    = 2 + 3 + 4 + 2
    = 11

### Examples

    letter_distance("sharp", "sharq") ➞ 1
    
    letter_distance("abcde", "Abcde") ➞ 32
    
    letter_distance("abcde", "bcdef") ➞ 5

### Notes

  * Always start comparing the two strings from their first letter.
  * Excess letters are not counted towards distance.
  * Capital letters are included.

"""

def letter_distance(txt1, txt2):
  a = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
  def l8r_dist(l1, l2, a):
    if l2 == 'A':
      return 32
    l1index = None
    l2index = None
    
    for n in range(26):
      tl8r = a[n]
      if tl8r == l1:
        l1index = n
      if tl8r == l2:
        l2index = n
      if l1index != None and l2index != None:
        break
    
    d = abs(l2index - l1index)
    
    return d
  
  txt_lengths = [len(txt1), len(txt2)]
  
  points = 0
  for n in range(0, min(txt_lengths)):
    
    tl1 = txt1[n]
    tl2 = txt2[n]
    
    if tl1 == tl2:
      points += 0
    else:
      points += l8r_dist(tl1, tl2, a)
  
  points += (max(txt_lengths) - min(txt_lengths))
  
  return points

