"""


Create a function that takes a single word string and does the following:

  1. Concatenates `inator` to the end if the word ends with a consonant, otherwise, concatenate `-inator` instead.

  2. Adds the word length of the original word to the end, supplied with "000".

The examples should make this clear.

### Examples

    inator_inator("Shrink") ➞ "Shrinkinator 6000"
    
    inator_inator("Doom") ➞ "Doominator 4000"
    
    inator_inator("EvilClone") ➞ "EvilClone-inator 9000"

### Notes

For the purposes of this challenge, vowels will be **a, e, i, o** and **u**
only.

"""

def inator_inator(inv): #w/o built-in
  def l(s):
    count = 0
    while s != "":
      count += 1
      s = s[1:]
    return count
  d = {1: "1", 2: "2",  3: "3", 4: "4", 5: "5",
  6: "6", 7: "7", 8: "8", 9: "9", 0: "0"}
  c, lst = l(inv), []
  while c > 0:
    lst += [c % 10]
    c //= 10
  lst, n = [d[x] for x in lst],  ""
  for i in lst:
    n += i
  if inv[-1] in 'aeiouAEIOU':
    return inv + "-inator " + n + "000"
  return inv + "inator " + n + "000"
​
def inator_inator(inv):
  return '{}-inator {}000'.format(inv, len(inv)) if inv[-1] in 'aeiouAEIOU' else\
  '{}inator {}000'.format(inv, len(inv))

