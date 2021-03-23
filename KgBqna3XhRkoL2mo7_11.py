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
    r = ""
    a  = "_abcdefghijklmnopqrstuvwxyz"
    while len(s) > 0:
        if "#" in s and s[2] == "#":
            r += a[int(s[:2])]
            s = s[3:]
        else:
            r += a[int(s[0])]
            s = s[1:]
    return r

