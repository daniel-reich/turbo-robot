"""


Create a solution that checks if a given string contains a sub-string pattern
repeated multiple times to return `True` or `False`.

### Examples

    repeated("a") ➞ False
    
    repeated("ababab") ➞ True
    
    repeated("aba") ➞ False
    
    repeated("abcabcabcabc") ➞ True
    
    repeated("aaxxtaaxztaaxxt") ➞ False

### Notes

Adroit programmers can solve this in one line.

"""

def repeated(s):
  if(len(s)<2):
    return False
  for i in range(0,len(s)):
    z=s[i+1:]
    check=0
    while(z.startswith(s[:i+1])):
      check=1
      z=z[len(s[:i+1]):]
    if(len(z)==0 and check==1):
      return True
  return False

