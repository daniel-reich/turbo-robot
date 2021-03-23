"""


Given a string `s` consisting from digits and `#`, translate `s` to English
lowercase characters as follows:

  * Characters ("a" to "i") are represented by ("1" to "9").
  * Characters ("j" to "z") are represented by ("10#" to "26#").

### Examples

    decrypt("10#11#12") ➞ "jkab"
    
    decrypt("1326#") ➞ "acz"
    
    decrypt("25#") ➞ "y"

### Notes

N/A

"""

def decrypt(s):
  A=[]
  i=0
  while i<len(s):
    if s[::-1][i]=='#':
      A.append(s[::-1][i+1:i+3])
      i+=3
    else:
      A.append(s[::-1][i])
      i+=1
  B=[x[::-1] for x in A][::-1]
  C=[int(x) for x in B]
  D=[chr(ord('a')+x-1) for x in C]
  return ''.join(D)

