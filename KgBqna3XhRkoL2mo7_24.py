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

def decrypt(st1):
    lst=[]
    i=0
    while i in range(len(st1)-2):
        if (st1[i+2]!='#'):
            if st1[i]!='#':
              lst.append(st1[i])
            i=i+1
        else:
            lst.append(st1[i:i+2])
            i=i+2
    ls=st1[-1]
    if ls!='#':
        for i in st1[-2:]:
          if i!='#':
            lst.append(i)
    return ("".join([chr(int(i)+96) for i in lst]))

