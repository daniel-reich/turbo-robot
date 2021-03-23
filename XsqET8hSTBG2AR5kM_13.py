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
    d = 0
    flag = 0
​
    if len(txt1) > len(txt2) or len(txt2) > len(txt1):
        flag = True
​
    if len(txt1) == len(txt2) or len(txt2) > len(txt1):
        N = len(txt1)
    else:
        N = len(txt2)
​
    for u in range(N):
         d += dist(ord(txt1[u]), ord(txt2[u]))
​
    if flag == 0:
        return d
    else:
        d += dist(len(txt1), len(txt2))
        return d
​
def dist(l1, l2):
    return abs(l1 - l2)

