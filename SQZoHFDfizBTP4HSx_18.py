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

def missing_alphabets(txt):
  
  full_alph = 'abcdefghijklmnopqrstuvwxyz'
  
  l8r_count = {}
  
  for l8r in full_alph:
    l8r_count[l8r] = txt.count(l8r)
  
  alph_nums = max(list(l8r_count.values()))
  
  tr = ''
  
  for l8r in full_alph:
    tr += (l8r * (alph_nums - l8r_count[l8r]))
  
  return tr

