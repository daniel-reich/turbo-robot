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

letters = {str(i - 96): chr(i) for i in range(97, 123)}
def decrypt(s):
    len_s = len(s)
    i = 0
    res = []
    while i < len_s:
        if i + 2 < len_s and s[i + 2] == "#":
            res.append(letters[s[i: i + 2]])
            i += 3
        else:
            res.append(letters[s[i: i + 1]])
            i += 1
    return "".join(res)

