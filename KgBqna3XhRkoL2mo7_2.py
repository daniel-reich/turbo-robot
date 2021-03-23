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
    ans = ""
    while len(s) >= 3:
        if s[2] == '#':
            ans += chr(96 + int(s[:2]))
            s = s[3:]
        else:
            ans += chr(96 + int(s[0]))
            s = s[1:]
    for c in s:
        ans += chr(96 + int(c))
    return ans

