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
  d = dict({str(i):chr(i+96) for i in range(1,11)},
      **{str(i)+'#':chr(i+96) for i in range(10,27)})
  i = 0
  ans =''
  
  while i <len(s):
    if i < len(s)-2 and s[i+2] == '#':  
      ans+=d[s[i:i+3]]
      i+= 3
    else:
      ans+= d[s[i]]
      i+=1
  
  return ans

