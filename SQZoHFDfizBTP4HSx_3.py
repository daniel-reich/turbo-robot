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
  sdict = {}
  a = 'abcdefghijklmnopqrstuvwxyz'
  s = ''
  
  for i in str:
    if i in sdict: sdict[i]+=1
    else: sdict[i] = 1
  
  kmax = sdict[max(sdict, key=sdict.get)]
  
  for l in a:
    if l not in sdict:
      s+=l*kmax
    elif sdict[l]<kmax:
      s+=l*(kmax-sdict[l])
      
  return s

