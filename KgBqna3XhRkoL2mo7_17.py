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
    d= {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '10#': 'j', '11#': 'k', '12#': 'l',
     '13#': 'm', '14#': 'n', '15#': 'o', '16#': 'p', '17#': 'q', '18#': 'r', '19#': 's', '20#': 't', '21#': 'u', '22#': 'v',
     '23#': 'w', '24#': 'x', '25#': 'y', '26#': 'z'}
    x = ''
    while True:
        if s in d.keys():
            x = x+d[s]
            return x
        for i in range(1,len(s)):
            if s[0:i*-1] in d.keys():
                x = x+ d[s[0:i*-1]]
                break
        s = s.replace(s[0:i*-1],'',1)
        if len(s) == 1:
            x = x+d[s]
            break
    return x

