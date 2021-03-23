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
      m = {}
      x = 'a'
      for i in range(1, 27):
         m[str(i)] = x
         x = chr(ord(x) + 1)
      ans = ""
      m['']=''
      i = len(s) - 1
      while i >= 0:
         if s[i] == "#":
            temp = ""
            for j in range(i - 2, i):
               temp += s[j]
            ans = m[str(temp)] + ans
            i -= 3
         else:
            ans = m[s[i]] + ans
            i -= 1
      return ans

