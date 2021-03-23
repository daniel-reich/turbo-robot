"""


Create a function that takes a string `txt` containing only letters from **a
to z** in lowercase and returns the **missing letter(s)** in alphabetical
order a-z.

  * A set of letters is given by `abcdefghijklmnopqrstuvwxyz`.
  * Two sets of alphabets means two or more alphabets.

### Examples

    missing_alphabets("abcdefghijklmnopqrstuvwxy") ➞ "z"
    # "z" is missing.
    
    missing_alphabets("aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyy") ➞ "zz"
    # Given string has a set of two alphabets so output will be "zz"
    
    missing_alphabets("edabit") ➞ "cfghjklmnopqrsuvwxyz"

### Notes

If the string contains all letters from `a-z`, return an empty string `""`.

"""

def missing_alphabets(n):
  c = {}
  for x in n:
    if c.get(x) == None:
      c[x] = 0
    c[x] += 1
  t = sorted(c.values())[-1]
  out = "".join([a*t for a in 'abcdefghijklmnopqrstuvwxyz'])
  for x in n:
    out = out.replace(x, '', 1)
  return out

