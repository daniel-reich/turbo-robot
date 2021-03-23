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
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    splitter = 0
    hold = ""
    for x in range(len(s)):
        if splitter == x:
            if splitter+2 < len(s):
                if s[splitter+2] == "#":
                    hold += alphabet[int(s[splitter:splitter+2])-1]
                    splitter += 2
                else:
                    hold += alphabet[int(s[splitter])-1]
                splitter += 1
            else:
                hold += alphabet[int(s[splitter])-1]
                splitter += 1
    return hold

