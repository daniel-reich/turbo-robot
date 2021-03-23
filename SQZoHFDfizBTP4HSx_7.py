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

def missing_alphabets (str):
  s = sorted(set(str))
  c = lambda x: str.count(x)
  if len(s)==26:
    return ''
  else:
    l = max([c(x) for x in s])
    mis = [chr(97+i) * (l-c(chr(97+i))) for i in range(26)
            if i >= len(s) or c(s[i])<l or ord(s[i]) != 97+i]
    return ''.join(mis)

