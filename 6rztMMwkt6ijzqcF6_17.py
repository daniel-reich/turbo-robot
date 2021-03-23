"""


This challenge concerns strings such as:

    "repeatedrepeatedrepeated"

... that are obtained by repeating a smaller string, which in this case is the
string `"repeated"`.

On a related note, since the string above is made of 3 repetitions, one way to
produce this string is via the code `3 * "repeated"`.

Write a function that, given a string, either:

  * Returns `False` if the string isn't made by repeating a smaller string or ...
  * Returns **the number of repetitions** if the string repeats a smaller string.

### Examples

    is_repeated("repeatedrepeatedrepeated") ➞ 3
    
    is_repeated("overintellectualizations") ➞ False
    
    is_repeated("nononononononononononono") ➞ 12
    
    is_repeated("moremoremoremoremoremore") ➞ 6
    
    is_repeated(",,,,,,,,,,,,,,,,,,,,,,,,") ➞ 24

### Notes

To keep things a little simpler, all strings in the tests will have length
exactly 24, just as in all the examples above. In particular, the answers will
always be divisors of 24.

"""

def is_repeated(strn):
  x = [24,12,8,6,4,3,2]
  for k in x:
    for i in range(int(24/k), 24):
      a = i
      while (a - (24/k)) >= 0:
        a = a - (24/k)
      if strn[int(a)] != strn[i]:
        break
      elif i == 23:
        return int(k)
  return False

