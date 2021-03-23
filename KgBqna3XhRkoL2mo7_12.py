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
  aToIu = '123456789'
  aToIs = 'abcdefghi'
  jToZu = ['10#','11#','12#','13#','14#','15#','16#','17#','18#','19#','20#','21#','22#','23#','24#','25#','26#']
  jToZs = 'jklmnopqrstuvwxyz'
  for i in range(len(jToZu)):
    s = s.replace(jToZu[i],jToZs[i])
  for i in range(len(aToIu)):
    s = s.replace(aToIu[i],aToIs[i])
  return s

